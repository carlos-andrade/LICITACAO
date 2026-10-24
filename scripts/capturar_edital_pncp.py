#!/usr/bin/env python3
"""Captura reutilizável de contratação PNCP: dados, itens, arquivos e base de cotação.
Uso:
  python scripts/capturar_edital_pncp.py --url URL --download-files
Requer: requests; openpyxl é opcional.
"""
from __future__ import annotations
import argparse, csv, hashlib, json, re, sys, time
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlparse, unquote
import requests

CONSULTA = "https://pncp.gov.br/api/consulta/v1"
PNCP = "https://pncp.gov.br/pncp-api/v1"
USER_AGENT = "LICITACAO-PNCP-Captura/1.0 (+https://github.com/carlos-andrade/LICITACAO)"
TIMEOUT = 40
MAX_FILE_BYTES = 150 * 1024 * 1024

def get(session, url, params=None):
    last = None
    for attempt in range(4):
        try:
            r = session.get(url, params=params, timeout=TIMEOUT, allow_redirects=True)
            if r.status_code == 404:
                return None, {"url": r.url, "http": 404, "error": "endpoint não encontrado"}
            if r.status_code == 429 or r.status_code >= 500:
                last = f"HTTP {r.status_code}"
                if attempt < 3:
                    time.sleep(min(2 ** (attempt + 1), 20))
                    continue
            r.raise_for_status()
            ctype = r.headers.get("content-type", "")
            try:
                body = r.json()
            except ValueError:
                body = None
            return body if body is not None else r.content, {
                "url": r.url, "http": r.status_code, "content_type": ctype,
                "bytes": len(r.content), "final_url": r.url
            }
        except Exception as e:
            last = str(e)
            if attempt < 3:
                time.sleep(min(2 ** (attempt + 1), 20))
    return None, {"url": url, "error": last or "falha desconhecida"}

def flatten(value, prefix=""):
    rows = []
    if isinstance(value, dict):
        for key, val in value.items():
            path = f"{prefix}.{key}" if prefix else str(key)
            rows.extend(flatten(val, path) if isinstance(val, (dict, list)) else [(path, val)])
    elif isinstance(value, list):
        for i, val in enumerate(value):
            rows.extend(flatten(val, f"{prefix}[{i}]"))
    else:
        rows.append((prefix, value))
    return rows

def listish(x):
    if isinstance(x, list):
        return [i for i in x if isinstance(i, dict)]
    if isinstance(x, dict):
        for k in ("data", "resultado", "content", "items", "itens", "arquivos", "historico", "resultados"):
            if isinstance(x.get(k), list):
                return [i for i in x[k] if isinstance(i, dict)]
    return []

def normalize_pncp_url(value):
    """Corrige URIs PNCP que publicam a porta interna 10240, mantendo host HTTPS público."""
    try:
        parsed = urlparse(value)
        if parsed.hostname == "pncp.gov.br" and parsed.port == 10240:
            return parsed._replace(netloc="pncp.gov.br").geturl()
    except (ValueError, AttributeError):
        pass
    return value

def find_urls(obj, base_url):
    found, seen = [], set()
    for key, value in flatten(obj):
        if isinstance(value, str) and value.startswith(("https://", "http://")):
            low = key.lower()
            if any(t in low for t in ("url", "arquivo", "documento", "anexo", "download", "link", "uri")):
                value = normalize_pncp_url(value)
                if value not in seen:
                    seen.add(value); found.append({"url": value, "campo": key, "origem": base_url})
    return found

def write_csv(path, rows, fields):
    with path.open("w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields, delimiter=";", extrasaction="ignore")
        w.writeheader()
        for row in rows: w.writerow(row)

def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--url", required=True, help="URL do edital no PNCP")
    ap.add_argument("--output-root", default="EDITAIS", help="Diretório raiz de saída")
    ap.add_argument("--download-files", action="store_true", help="Baixa anexos encontrados, com hash SHA-256")
    ap.add_argument("--no-supplier-template", action="store_true")
    args = ap.parse_args()
    parsed = urlparse(args.url)
    match = re.fullmatch(r"/app/editais/(\d{14})/(\d{4})/(\d+)", parsed.path)
    if parsed.hostname not in ("pncp.gov.br", "www.pncp.gov.br") or not match:
        ap.error("URL inválida. Use https://pncp.gov.br/app/editais/{CNPJ}/{ANO}/{SEQUENCIAL}")
    cnpj, year_s, seq_s = match.groups()
    year, seq = int(year_s), int(seq_s)
    folder = Path(args.output_root) / f"CONTRATACAO-{cnpj}-{year}-{seq}"
    folder.mkdir(parents=True, exist_ok=True)
    session = requests.Session()
    session.headers.update({"User-Agent": USER_AGENT, "Accept": "application/json, */*"})
    stamp = datetime.now(timezone.utc).isoformat(timespec="seconds")
    api_root = f"{PNCP}/orgaos/{cnpj}/compras/{year}/{seq}"
    consulta_root = f"{CONSULTA}/orgaos/{cnpj}/compras/{year}/{seq}"
    endpoints = [
        ("geral_consulta", consulta_root, None),
        ("geral_pncp", api_root, None),
        ("itens", f"{api_root}/itens", {"pagina": 1, "tamanhoPagina": 100}),
        ("arquivos", f"{api_root}/arquivos", {"pagina": 1, "tamanhoPagina": 100}),
        # O endpoint de arquivos pode expor metadados por lista e/ou por ID.
        # Consultar IDs sequenciais permite recuperar anexos mesmo quando a lista falha.
        *[(f"arquivo_{i}", f"{api_root}/arquivos/{i}", None) for i in range(1, 21)],
        ("historico", f"{api_root}/historico", {"pagina": 1, "tamanhoPagina": 100}),
        ("atas", f"{api_root}/atas", {"pagina": 1, "tamanhoPagina": 100}),
        ("contratos", f"{api_root}/contratos", {"pagina": 1, "tamanhoPagina": 100}),
        ("empenhos", f"{api_root}/empenhos", {"pagina": 1, "tamanhoPagina": 100}),
    ]
    responses, diagnostics = {}, []
    for name, url, params in endpoints:
        payload, diag = get(session, url, params)
        diagnostics.append({"secao": name, **diag})
        if payload is not None:
            if isinstance(payload, bytes):
                binary_dir = folder / "arquivos_originais"
                binary_dir.mkdir(exist_ok=True)
                dest = binary_dir / f"{name}.bin"
                dest.write_bytes(payload)
                responses[name] = {"binary_response": True, "bytes": len(payload), "arquivo_local": str(dest), "sha256": hashlib.sha256(payload).hexdigest()}
            else:
                responses[name] = payload
        time.sleep(0.25)

    # Paginação adicional nas seções de listas, quando a resposta anuncia mais páginas.
    for name, url, _ in endpoints:
        if name not in ("itens", "arquivos", "historico", "atas", "contratos", "empenhos"):
            continue
        first = responses.get(name)
        if not isinstance(first, dict):
            continue
        total = first.get("totalPaginas") or first.get("totalPaginasEncontradas") or first.get("pages")
        try: total = min(int(total), 100) if total else 1
        except (ValueError, TypeError): total = 1
        if total <= 1: continue
        pages = [first]
        for page in range(2, total + 1):
            payload, diag = get(session, url, {"pagina": page, "tamanhoPagina": 100})
            diagnostics.append({"secao": name, "pagina": page, **diag})
            if payload is not None and isinstance(payload, dict): pages.append(payload)
            else: break
            time.sleep(0.2)
        responses[name] = {"paginas_capturadas": pages, "total_paginas_reportado": total}

    all_links = []
    for name, payload in responses.items():
        if not isinstance(payload, (dict, list)): continue
        all_links.extend(find_urls(payload, name))
    unique = []
    seen = set()
    for link in all_links:
        if link["url"] not in seen:
            seen.add(link["url"]); unique.append(link)

    downloads = []
    if args.download_files:
        files_dir = folder / "arquivos_originais"
        files_dir.mkdir(exist_ok=True)
        for index, link in enumerate(unique, 1):
            try:
                with session.get(link["url"], stream=True, timeout=TIMEOUT, allow_redirects=True) as r:
                    if not r.ok:
                        downloads.append({**link, "status": f"HTTP {r.status_code}"}); continue
                    disposition = r.headers.get("content-disposition", "")
                    filename_match = re.search(r'filename\*?=(?:UTF-8\'\')?["]?([^";]+)', disposition, re.I)
                    filename = unquote(filename_match.group(1).strip('"')) if filename_match else Path(urlparse(r.url).path).name
                    filename = re.sub(r"[^A-Za-z0-9._-]+", "_", filename)[:150] or f"anexo-{index}.bin"
                    dest = files_dir / f"{index:03d}-{filename}"
                    h = hashlib.sha256(); size = 0
                    with dest.open("wb") as f:
                        for chunk in r.iter_content(128 * 1024):
                            if not chunk: continue
                            size += len(chunk)
                            if size > MAX_FILE_BYTES:
                                raise ValueError("arquivo excede limite de 150 MiB")
                            f.write(chunk); h.update(chunk)
                    downloads.append({**link, "status": "baixado", "arquivo_local": str(dest), "bytes": size, "sha256": h.hexdigest(), "url_final": r.url})
            except Exception as e:
                downloads.append({**link, "status": f"falha: {e}"})

    general = responses.get("geral_consulta") or responses.get("geral_pncp") or {}
    item_payload = responses.get("itens", {})
    item_rows = listish(item_payload)
    if not item_rows and isinstance(item_payload, dict) and "paginas_capturadas" in item_payload:
        item_rows = [row for page in item_payload["paginas_capturadas"] for row in listish(page)]
    normalized_items = []
    for idx, item in enumerate(item_rows, 1):
        unit = item.get("unidadeMedida") if isinstance(item.get("unidadeMedida"), dict) else {}
        normalized_items.append({
            "numero_item": item.get("numeroItem", item.get("sequencialItem", idx)),
            "descricao": item.get("descricao", item.get("descricaoItem", "")),
            "descricao_detalhada": item.get("descricaoDetalhada", item.get("descricaoComplementar", "")),
            "quantidade": item.get("quantidade", ""),
            "unidade": unit.get("nome", unit.get("sigla", item.get("unidadeMedidaNome", ""))),
            "valor_unitario_estimado": item.get("valorUnitarioEstimado", item.get("valorUnitario", "")),
            "valor_total_estimado": item.get("valorTotal", item.get("valorTotalEstimado", "")),
            "situacao": item.get("situacaoCompraItemNome", item.get("situacaoItem", "")),
            "criterio_julgamento": item.get("criterioJulgamentoNome", item.get("criterioJulgamento", "")),
        })

    meta = {
        "status": "CAPTURA_COM_DADOS" if responses else "FALHA",
        "capturado_em_utc": stamp, "url_contratacao": args.url,
        "identificacao": {"cnpj": cnpj, "ano": year, "sequencial": seq, "numero_controle_esperado": f"{cnpj}-1-{seq:06d}/{year}"},
        "fonte_primaria": "Portal Nacional de Contratações Públicas (PNCP)",
        "endpoints_consultados": [{"secao": n, "url": u, "parametros": p} for n, u, p in endpoints],
        "diagnostico_http": diagnostics, "quantidade_respostas_capturadas": len(responses),
        "quantidade_itens_normalizados": len(normalized_items), "quantidade_links_detectados": len(unique),
        "quantidade_arquivos_baixados": sum(1 for d in downloads if d.get("status") == "baixado"),
        "avisos": [
            "Captura best-effort: HTTP 404 em endpoint opcional não prova inexistência de dados.",
            "Confira diagnóstico, paginação e os documentos oficiais antes de decidir.",
            "O conteúdo original é preservado no JSON; campos normalizados dependem dos nomes de campo retornados pela API.",
            "Nenhum preço de fornecedor é inventado ou considerado cotação confirmada."
        ]
    }
    (folder / "captura-bruta.json").write_text(json.dumps({"metadados": meta, "respostas_api": responses, "links_arquivos": unique, "downloads": downloads}, ensure_ascii=False, indent=2), encoding="utf-8")
    write_csv(folder / "todos-os-campos.csv",
              [{"secao": name, "campo": k, "valor": json.dumps(v, ensure_ascii=False) if isinstance(v, (dict, list)) else str(v)} for name, payload in responses.items() if isinstance(payload, (dict, list)) for k, v in flatten(payload)],
              ["secao", "campo", "valor"])
    write_csv(folder / "itens.csv", normalized_items,
              ["numero_item", "descricao", "descricao_detalhada", "quantidade", "unidade", "valor_unitario_estimado", "valor_total_estimado", "situacao", "criterio_julgamento"])
    write_csv(folder / "arquivos.csv", unique, ["url", "campo", "origem"])
    write_csv(folder / "downloads.csv", downloads, ["url", "campo", "origem", "status", "arquivo_local", "bytes", "sha256", "url_final"])
    if not args.no_supplier_template:
        supplier_rows = []
        for item in normalized_items or [{"numero_item": "", "descricao": "Preencher após confirmar itens no PNCP"}]:
            for n in range(1, 11):
                supplier_rows.append({
                    "numero_item": item.get("numero_item", ""), "descricao_item": item.get("descricao", ""),
                    "fornecedor": "", "cnpj_fornecedor": "", "url_fonte": "", "data_hora_consulta": "",
                    "preco_anunciado": "", "frete": "", "tributos_taxas": "", "preco_total_entregue": "",
                    "estoque_confirmado": "", "prazo_entrega": "", "validade_oferta": "",
                    "especificacao_confirmada": "", "contato_confirmacao": "", "status_validacao": "PENDENTE",
                    "observacoes": f"Slot de pesquisa {n}; não é fornecedor nem cotação."
                })
        write_csv(folder / "pesquisa-fornecedores-template.csv", supplier_rows, list(supplier_rows[0].keys()))
    try:
        from openpyxl import Workbook
        wb = Workbook()
        ws = wb.active; ws.title = "Dados brutos"
        ws.append(["secao", "campo", "valor"])
        for name, payload in responses.items():
            if isinstance(payload, (dict, list)):
                for k, v in flatten(payload):
                    ws.append([name, k, json.dumps(v, ensure_ascii=False) if isinstance(v, (dict, list)) else str(v)])
        for sheet in wb.worksheets:
            sheet.freeze_panes = "A2"; sheet.auto_filter.ref = sheet.dimensions
            for col, width in zip("ABC", [24, 48, 90]): sheet.column_dimensions[col].width = width
        wb.save(folder / "captura-pncp.xlsx")
    except ImportError:
        pass
    print(json.dumps({"status": meta["status"], "pasta": str(folder), "respostas": len(responses), "itens": len(normalized_items), "links_arquivos": len(unique), "baixados": meta["quantidade_arquivos_baixados"], "fornecedores": "template de 10 linhas por item; não são cotações"}, ensure_ascii=False, indent=2))
    return 0 if responses else 2

if __name__ == "__main__":
    try: raise SystemExit(main())
    except KeyboardInterrupt: raise SystemExit(130)
