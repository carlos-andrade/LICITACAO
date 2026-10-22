#!/usr/bin/env python3
"""Captura pública de contratação PNCP em Markdown, CSV e JSON bruto.
Instale: pip install requests beautifulsoup4
Uso: python pncp_capture.py "https://pncp.gov.br/app/editais/33663683000116/2026/548" --output-dir EDITAIS --download-docs
"""
import argparse, csv, json, re, sys
from datetime import datetime
from pathlib import Path
from urllib.parse import urlparse, urljoin
import requests
from bs4 import BeautifulSoup

API = "https://pncp.gov.br/api/consulta/v1"
TIMEOUT = 25
MAX_BYTES = 80 * 1024 * 1024
S = requests.Session()
S.headers.update({"User-Agent": "LICITACAO-PNCP-Capture/1.0", "Accept": "application/json, text/html, */*"})

def fetch(url):
    try:
        r = S.get(url, timeout=TIMEOUT)
        if not r.ok:
            return None, f"HTTP {r.status_code}"
        try:
            return r.json(), f"HTTP {r.status_code} JSON"
        except ValueError:
            return r.text, f"HTTP {r.status_code} texto"
    except requests.RequestException as exc:
        return None, f"ERRO: {exc}"

def parse_url(url):
    p = urlparse(url)
    if p.scheme not in ("http", "https") or p.hostname not in ("pncp.gov.br", "www.pncp.gov.br"):
        raise ValueError("Use um link público de pncp.gov.br")
    m = re.search(r"/app/(?:editais|contratos|atas)/(\d{14})/(\d{4})/(\d+)", p.path)
    if not m:
        raise ValueError("Formato esperado: /app/editais/{CNPJ}/{ano}/{sequencial}")
    return m.groups()

def flatten(obj, prefix=""):
    rows = []
    if isinstance(obj, dict):
        for k, v in obj.items():
            key = f"{prefix}.{k}" if prefix else str(k)
            rows.extend(flatten(v, key) if isinstance(v, (dict, list)) else [(key, v)])
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            rows.extend(flatten(v, f"{prefix}[{i}]"))
    else:
        rows.append((prefix, obj))
    return rows

def text(value):
    if value is None:
        return ""
    if isinstance(value, (dict, list)):
        return json.dumps(value, ensure_ascii=False)
    return str(value)

def find_key(obj, terms):
    for key, value in flatten(obj):
        if any(term in key.lower() for term in terms) and value not in (None, ""):
            return text(value)
    return ""

def safe_name(value):
    return re.sub(r"-+", "-", re.sub(r"[^A-Za-z0-9._-]+", "-", value)).strip("-")[:90] or "pncp"

def extract_html(url):
    body, status = fetch(url)
    if not isinstance(body, str):
        return {}, [], status
    soup = BeautifulSoup(body, "html.parser")
    metadata, links, seen = {}, [], set()
    for tag in soup.find_all("meta"):
        key, value = tag.get("property") or tag.get("name"), tag.get("content")
        if key and value:
            metadata[f"meta:{key}"] = value
    for tag in soup.find_all("script", attrs={"type": "application/ld+json"}):
        try:
            metadata.setdefault("jsonld", []).append(json.loads(tag.string or tag.get_text()))
        except (ValueError, TypeError):
            pass
    for anchor in soup.find_all("a", href=True):
        href = urljoin(url, anchor["href"])
        if href not in seen and urlparse(href).scheme in ("http", "https"):
            seen.add(href)
            links.append({"texto": " ".join(anchor.get_text(" ", strip=True).split()), "url": href})
    return metadata, links, status

def list_payload(payload):
    if isinstance(payload, list):
        return [item for item in payload if isinstance(item, dict)]
    if isinstance(payload, dict):
        for key, value in payload.items():
            if isinstance(value, list) and ("item" in key.lower() or all(isinstance(x, dict) for x in value)) and value:
                return [item for item in value if isinstance(item, dict)]
        return [payload]
    return []

def normalize_items(payload):
    rows = []
    for index, item in enumerate(list_payload(payload), 1):
        get = lambda *terms: find_key(item, tuple(term.lower() for term in terms))
        rows.append({
            "numero": get("numeroitem", "sequencialitem") or str(index),
            "codigo": get("codigocatmat", "codigocatser", "catmat", "catser", "codigoitem"),
            "descricao": get("descricao", "objeto", "nomeitem"),
            "tipo": get("materialouservico"),
            "unidade": get("unidademedida", "unidadefornecimento", "unidade"),
            "quantidade": get("quantidade"),
            "valor_unitario": get("valorunitarioestimado", "valorunitario"),
            "valor_total": get("valortotalestimado", "valortotal"),
            "orcamento_sigiloso": get("orcamentosigiloso"),
            "json_item": json.dumps(item, ensure_ascii=False),
        })
    return rows

def extract_documents(payload):
    if isinstance(payload, dict):
        for key, value in payload.items():
            if any(term in key.lower() for term in ("documento", "arquivo")) and isinstance(value, list) and value and all(isinstance(x, dict) for x in value):
                return value
        for value in payload.values():
            found = extract_documents(value)
            if found:
                return found
    elif isinstance(payload, list):
        for value in payload:
            found = extract_documents(value)
            if found:
                return found
    return []

def download(url, destination):
    try:
        with S.get(url, stream=True, timeout=TIMEOUT) as response:
            if not response.ok:
                return f"HTTP {response.status_code}"
            total = 0
            with open(destination, "wb") as output:
                for chunk in response.iter_content(131072):
                    if not chunk:
                        continue
                    total += len(chunk)
                    if total > MAX_BYTES:
                        output.close()
                        Path(destination).unlink(missing_ok=True)
                        return "Limite de tamanho excedido"
                    output.write(chunk)
            return f"Baixado: {total} bytes"
    except requests.RequestException as exc:
        return f"ERRO: {exc}"

def main():
    parser = argparse.ArgumentParser(description="Captura dados de uma contratação pública no PNCP.")
    parser.add_argument("url")
    parser.add_argument("--output-dir", default="EDITAIS")
    parser.add_argument("--download-docs", action="store_true")
    args = parser.parse_args()
    cnpj, year, sequence = parse_url(args.url)
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    stem = safe_name(f"{year}-{sequence}-{cnpj}")
    base = f"{API}/orgaos/{cnpj}/compras/{year}/{sequence}"
    captured = datetime.now().astimezone().isoformat(timespec="seconds")
    diagnostics, raw = [], {}
    endpoints = {"contratacao": base, "itens": base + "/itens", "documentos": base + "/arquivos", "historico": base + "/historico"}
    for name, endpoint in endpoints.items():
        payload, status = fetch(endpoint)
        diagnostics.append({"etapa": name, "url": endpoint, "resultado": status})
        if payload is not None:
            raw[name] = payload
    page_metadata, page_links, page_status = extract_html(args.url)
    diagnostics.append({"etapa": "html", "url": args.url, "resultado": page_status})
    items = normalize_items(raw.get("itens"))
    documents = extract_documents(raw.get("documentos"))
    downloads = []
    if args.download_docs:
        folder = output_dir / (stem + "_documentos")
        folder.mkdir(exist_ok=True)
        for index, document in enumerate(documents, 1):
            url = find_key(document, ("url",))
            title = find_key(document, ("titulo", "nomearquivo")) or f"documento-{index}"
            if not url.startswith("http"):
                downloads.append({"titulo": title, "url": url, "resultado": "URL não retornada"})
                continue
            extension = Path(urlparse(url).path).suffix.lower()
            if extension not in (".pdf", ".doc", ".docx", ".xls", ".xlsx", ".zip", ".png", ".jpg", ".jpeg"):
                extension = ".bin"
            destination = folder / f"{index:03d}-{safe_name(title)}{extension}"
            downloads.append({"titulo": title, "url": url, "arquivo": str(destination), "resultado": download(url, destination)})
    raw_path = output_dir / (stem + "-captura-bruta.json")
    raw_doc = {"url": args.url, "capturado_em": captured, "identificador": {"cnpj": cnpj, "ano": year, "sequencial": sequence},
               "diagnosticos": diagnostics, "html_metadata": page_metadata, "links_pagina": page_links,
               "documentos_api": documents, "downloads": downloads, "respostas_api": raw}
    raw_path.write_text(json.dumps(raw_doc, ensure_ascii=False, indent=2), encoding="utf-8")
    lines = [f"# Captura PNCP — {cnpj}/{year}/{sequence}", "", f"- **URL:** {args.url}",
             f"- **Data/hora:** {captured}", f"- **JSON bruto:** `{raw_path.name}`", "",
             "## Diagnóstico das fontes", "", "| Etapa | URL | Resultado |", "|---|---|---|"]
    for diagnostic in diagnostics:
        lines.append(f"| {diagnostic['etapa']} | {diagnostic['url']} | {diagnostic['resultado'].replace('|', '/')} |")
    lines += ["", "## Tabela de itens retornados pela API", ""]
    columns = ["numero", "codigo", "descricao", "tipo", "unidade", "quantidade", "valor_unitario", "valor_total", "orcamento_sigiloso"]
    if items:
        lines += ["| Nº | Código CATMAT/CATSER | Descrição | Tipo | Unidade | Quantidade | Valor unitário | Valor total | Orçamento sigiloso |",
                  "|---|---|---|---|---|---:|---:|---:|---|"]
        for row in items:
            cells = [(row[column] or "Não retornado").replace("|", "\\|").replace("\n", " ") for column in columns]
            lines.append("| " + " | ".join(cells) + " |")
        csv_path = output_dir / (stem + "-itens.csv")
        with csv_path.open("w", newline="", encoding="utf-8-sig") as output:
            writer = csv.DictWriter(output, fieldnames=items[0].keys())
            writer.writeheader()
            writer.writerows(items)
        lines += ["", f"CSV detalhado: `{csv_path.name}`."]
    else:
        lines += ["Nenhum item foi normalizado. Pode indicar API indisponível ou formato não reconhecido; não significa ausência de itens."]
    lines += ["", "## Metadados e campos retornados", "", "| Campo | Valor |", "|---|---|"]
    flattened = flatten(page_metadata) + (flatten({"api.contratacao": raw["contratacao"]}) if "contratacao" in raw else [])
    for key, value in flattened:
        lines.append("| " + key.replace("|", "/") + " | " + text(value).replace("|", "\\|").replace("\n", " ") + " |")
    if documents:
        lines += ["", "## Documentos identificados", "", "| Nº | Título | Tipo | Data publicação | URL |", "|---:|---|---|---|---|"]
        for index, document in enumerate(documents, 1):
            values = [str(index), find_key(document, ("titulo", "nomearquivo")) or f"Documento {index}",
                      find_key(document, ("tipodocumentonome", "tipodocumentoid")), find_key(document, ("datapublicacaopncp",)),
                      find_key(document, ("url",)) or "Não retornada"]
            lines.append("| " + " | ".join(value.replace("|", "\\|") for value in values) + " |")
    else:
        lines += ["", "## Documentos identificados", "", "A consulta não retornou lista de documentos reconhecível."]
    if downloads:
        lines += ["", "## Tentativas de download", "", "| Documento | URL | Resultado |", "|---|---|---|"]
        for record in downloads:
            lines.append(f"| {record['titulo']} | {record['url']} | {record['resultado']} |")
    lines += ["", "## Links capturados da página", "", "| Texto | URL |", "|---|---|"]
    for link in page_links:
        lines.append("| " + (link["texto"] or "(sem rótulo)").replace("|", "/") + " | " + link["url"] + " |")
    lines += ["", "## Limitações", "", "- O relatório contém apenas os dados devolvidos pela API e pelo HTML.",
              "- Baixar um PDF não significa extrair o texto e as tabelas nele contidos; aplique extração PDF/OCR em separado quando necessário.",
              "- Confira diagnósticos HTTP, anexos e retificações antes de utilizar a análise comercial.",
              "- Campo vazio não prova que a informação inexiste.", "",
              "Documentação: [API de Consulta PNCP](https://pncp.gov.br/api/consulta/swagger-ui/index.html) · [Manual PNCP](https://pncp.gov.br/manual/pt-br/latest/)", ""]
    markdown_path = output_dir / (stem + "-tabela-capturada.md")
    markdown_path.write_text("\n".join(lines), encoding="utf-8")
    print("Markdown:", markdown_path)
    print("JSON bruto:", raw_path)
    print("Itens:", len(items), "; documentos:", len(documents))
    print("Revise os diagnósticos HTTP; campos ausentes não são considerados inexistentes.")

if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print("ERRO:", exc, file=sys.stderr)
        sys.exit(2)
