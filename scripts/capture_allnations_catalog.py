#!/usr/bin/env python3
"""Captura produtos publicamente acessíveis no site All Nations.

Uso:
  python scripts/capture_allnations_catalog.py
  python scripts/capture_allnations_catalog.py --output FORNECEDORES/allnations-produtos.csv
  python scripts/capture_allnations_catalog.py --max-pages 150 --delay 1.5

O script não contorna login, CAPTCHA, bloqueios, nem restrições do robots.txt.
Só inclui produtos quando a página expõe dados legíveis publicamente.
Preço pode estar ausente em catálogo B2B; não é inventado.
"""
from __future__ import annotations

import argparse
import csv
import json
import re
import sys
import time
import urllib.robotparser
from collections import deque
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from urllib.parse import urljoin, urlparse, urldefrag

import requests
from bs4 import BeautifulSoup

BASE = "https://allnations.com.br/"
DOMAIN = "allnations.com.br"
USER_AGENT = "LICITACAO-CatalogCapture/1.0 (+https://github.com/carlos-andrade/LICITACAO)"
PRODUCT_TERMS = (
    "produto", "product", "item", "sku", "gtin", "mpn", "brand",
    "offers", "offer", "price", "availability", "productgroup",
)
SKIP_EXTENSIONS = (".pdf", ".jpg", ".jpeg", ".png", ".gif", ".webp", ".svg",
                   ".zip", ".rar", ".7z", ".mp4", ".mp3", ".css", ".js")
COLUMNS = [
    "capturado_em_utc", "nome", "marca", "modelo", "sku", "gtin",
    "categoria", "preco", "moeda", "disponibilidade", "url_produto",
    "origem_dado", "status_captura", "observacoes",
]

def normalize_url(url: str, base: str = BASE) -> str | None:
    # Some legacy menu links contain literal backslashes; browsers treat them as slashes.
    raw = url.strip().replace("\\\\", "/").replace("\\", "/")
    url = urldefrag(urljoin(base, raw))[0]
    p = urlparse(url)
    if p.scheme not in ("http", "https") or p.hostname not in (DOMAIN, "www." + DOMAIN):
        return None
    path = re.sub(r"/{2,}", "/", p.path or "/")
    # Canonicalize host and remove fragments/tracking-only query parameters.
    host = DOMAIN
    query_items = []
    for key, value in __import__("urllib.parse", fromlist=["parse_qsl"]).parse_qsl(p.query, keep_blank_values=True):
        low = key.lower()
        if low.startswith("utm_") or low in {"gclid", "fbclid", "msclkid", "ref", "source"}:
            continue
        query_items.append((key, value))
    from urllib.parse import urlencode
    query = urlencode(query_items, doseq=True)
    normalized = p._replace(netloc=host, path=path, query=query, fragment="").geturl()
    if path.lower().endswith(SKIP_EXTENSIONS):
        return None
    # Do not crawl account, checkout, order, or payment flows.
    blocked = ("/minhaconta", "/minha-conta", "/pedido", "/checkout", "/carrinho", "/cart", "/login", "/register")
    if any(path.lower().startswith(x) for x in blocked):
        return None
    return normalized

def text(value: Any) -> str:
    if value is None:
        return ""
    if isinstance(value, (dict, list)):
        return json.dumps(value, ensure_ascii=False)
    return re.sub(r"\s+", " ", str(value)).strip()

def walk_jsonld(node: Any):
    if isinstance(node, dict):
        typ = node.get("@type", "")
        types = typ if isinstance(typ, list) else [typ]
        if any(str(t).lower() in ("product", "productgroup") for t in types):
            yield node
        graph = node.get("@graph")
        if graph:
            yield from walk_jsonld(graph)
        for k, v in node.items():
            if k != "@graph" and isinstance(v, (dict, list)):
                yield from walk_jsonld(v)
    elif isinstance(node, list):
        for item in node:
            yield from walk_jsonld(item)

def first(*values: Any) -> str:
    for value in values:
        if value not in (None, "", [], {}):
            if isinstance(value, dict):
                return text(value.get("name") or value.get("@id") or value)
            if isinstance(value, list):
                if value:
                    return first(*value)
            else:
                return text(value)
    return ""

def price_from_product(p: dict[str, Any]) -> tuple[str, str, str]:
    offers = p.get("offers")
    if isinstance(offers, list):
        offers = offers[0] if offers else {}
    offers = offers if isinstance(offers, dict) else {}
    price = first(offers.get("price"), offers.get("lowPrice"), offers.get("highPrice"))
    currency = first(offers.get("priceCurrency"))
    availability = first(offers.get("availability"))
    if availability:
        availability = availability.rsplit("/", 1)[-1]
    return price, currency, availability

def category_from_product(p: dict[str, Any], soup: BeautifulSoup) -> str:
    cat = first(p.get("category"))
    if cat:
        return cat
    crumbs = []
    for el in soup.select('[aria-label*="breadcrumb" i] a, .breadcrumb a, .breadcrumbs a, nav.breadcrumb a'):
        t = text(el.get_text(" "))
        if t and t.lower() not in ("home", "início", "inicio"):
            crumbs.append(t)
    return " > ".join(crumbs)

def product_row(p: dict[str, Any], url: str, soup: BeautifulSoup, timestamp: str) -> dict[str, str]:
    offers = p.get("offers") if isinstance(p.get("offers"), dict) else {}
    price, currency, availability = price_from_product(p)
    brand = p.get("brand")
    model = first(p.get("model"), p.get("mpn"))
    return {
        "capturado_em_utc": timestamp,
        "nome": first(p.get("name"), p.get("alternateName")),
        "marca": first(brand.get("name") if isinstance(brand, dict) else brand),
        "modelo": model,
        "sku": first(p.get("sku"), p.get("productID")),
        "gtin": first(p.get("gtin13"), p.get("gtin14"), p.get("gtin12"), p.get("gtin8"), p.get("gtin")),
        "categoria": category_from_product(p, soup),
        "preco": price,
        "moeda": currency,
        "disponibilidade": availability,
        "url_produto": url,
        "origem_dado": "JSON-LD/Product",
        "status_captura": "capturado",
        "observacoes": "Campos ausentes não foram inferidos; preço pode depender de login/cadastro B2B.",
    }

def meta_product(soup: BeautifulSoup, url: str, timestamp: str) -> dict[str, str] | None:
    def meta(*names: str) -> str:
        for n in names:
            tag = soup.find("meta", attrs={"property": n}) or soup.find("meta", attrs={"name": n})
            if tag and tag.get("content"):
                return text(tag["content"])
        return ""
    name = meta("og:title", "twitter:title")
    typ = meta("og:type")
    if not name or ("product" not in typ.lower() and not soup.select_one('[itemtype*="schema.org/Product"]')):
        return None
    return {
        "capturado_em_utc": timestamp, "nome": name,
        "marca": meta("product:brand"), "modelo": meta("product:retailer_item_id"),
        "sku": meta("product:retailer_item_id"), "gtin": "",
        "categoria": "", "preco": meta("product:price:amount"),
        "moeda": meta("product:price:currency"),
        "disponibilidade": meta("product:availability"),
        "url_produto": url, "origem_dado": "Open Graph/meta",
        "status_captura": "capturado_com_campos_limitados",
        "observacoes": "Metadados estruturados incompletos; confirmar página de origem.",
    }

def main() -> int:
    parser = argparse.ArgumentParser(description="Captura catálogo público All Nations para CSV/JSON.")
    parser.add_argument("--start-url", default=urljoin(BASE, "all"))
    parser.add_argument("--output", default="FORNECEDORES/allnations-produtos.csv")
    parser.add_argument("--json-output", default="FORNECEDORES/allnations-produtos.json")
    parser.add_argument("--max-pages", type=int, default=300)
    parser.add_argument("--delay", type=float, default=1.0)
    parser.add_argument("--timeout", type=float, default=20)
    parser.add_argument("--ignore-robots", action="store_true",
                        help="Não usar esta opção sem autorização explícita do proprietário do site.")
    args = parser.parse_args()

    start = normalize_url(args.start_url)
    if not start:
        print("Erro: --start-url precisa pertencer a allnations.com.br", file=sys.stderr)
        return 2

    session = requests.Session()
    session.headers.update({"User-Agent": USER_AGENT, "Accept-Language": "pt-BR,pt;q=0.9,en;q=0.7"})
    robots = urllib.robotparser.RobotFileParser()
    robots.set_url(urljoin(BASE, "/robots.txt"))
    try:
        robots.read()
    except Exception as exc:
        print(f"Aviso: não foi possível ler robots.txt ({exc}); será aplicado modo conservador.")
        if not args.ignore_robots:
            print("Encerrando por segurança. Confira robots.txt ou use --ignore-robots somente com autorização.", file=sys.stderr)
            return 3

    def allowed(url: str) -> bool:
        if args.ignore_robots:
            return True
        try:
            return robots.can_fetch(USER_AGENT, url) and robots.can_fetch("*", url)
        except Exception:
            return False

    if not allowed(start):
        print(f"robots.txt não permite capturar {start}. Encerrado sem contornar a regra.", file=sys.stderr)
        return 3

    queue = deque([start])
    # Discover public sitemap URLs where permitted, to improve catalog coverage.
    sitemap_candidates = [urljoin(BASE, "/sitemap.xml"), urljoin(BASE, "/sitemap_index.xml")]
    for sitemap_url in sitemap_candidates:
        if not allowed(sitemap_url):
            continue
        try:
            sitemap_response = session.get(sitemap_url, timeout=args.timeout)
            if sitemap_response.ok and "xml" in sitemap_response.headers.get("Content-Type", "").lower():
                sitemap_soup = BeautifulSoup(sitemap_response.text, "xml")
                for loc in sitemap_soup.find_all("loc"):
                    candidate = normalize_url(loc.get_text(strip=True))
                    if candidate and candidate not in queue:
                        queue.append(candidate)
        except requests.RequestException as exc:
            errors.append({"url": sitemap_url, "status": "erro_sitemap", "erro": str(exc)[:300]})
    visited: set[str] = set()
    found_products: dict[str, dict[str, str]] = {}
    errors: list[dict[str, str]] = []
    started = datetime.now(timezone.utc).isoformat(timespec="seconds")
    pages_ok = 0

    while queue and len(visited) < args.max_pages:
        url = queue.popleft()
        if url in visited or not allowed(url):
            continue
        visited.add(url)
        try:
            response = session.get(url, timeout=args.timeout, allow_redirects=True)
            final_url = normalize_url(response.url)
            if not final_url:
                continue
            if response.status_code in (401, 403, 429):
                errors.append({"url": url, "status": str(response.status_code),
                               "erro": "Acesso restrito/limite; sem tentativa de contorno."})
                continue
            response.raise_for_status()
            content_type = response.headers.get("Content-Type", "").lower()
            if "html" not in content_type and not response.text.lstrip().startswith("<!doctype html"):
                continue
            soup = BeautifulSoup(response.text, "html.parser")
            pages_ok += 1
            timestamp = datetime.now(timezone.utc).isoformat(timespec="seconds")

            jsonld_products = []
            for tag in soup.find_all("script", attrs={"type": re.compile("ld\+json", re.I)}):
                try:
                    obj = json.loads(tag.string or tag.get_text())
                    jsonld_products.extend(walk_jsonld(obj))
                except (ValueError, TypeError):
                    continue
            for product in jsonld_products:
                row = product_row(product, final_url, soup, timestamp)
                if row["nome"]:
                    row["url_produto"] = first(product.get("url"), final_url)
                    normalized = normalize_url(row["url_produto"], final_url) or final_url
                    row["url_produto"] = normalized
                    found_products[normalized] = row

            if not jsonld_products:
                row = meta_product(soup, final_url, timestamp)
                if row and row["nome"]:
                    found_products[final_url] = row

            for a in soup.find_all("a", href=True):
                href = normalize_url(a["href"], final_url)
                if href and href not in visited and href not in queue:
                    # Avoid query-explosion from faceted search/session URLs.
                    p = urlparse(href)
                    if p.query and any(x in p.query.lower() for x in ("session", "token", "sid", "sort", "filter")):
                        continue
                    queue.append(href)

            time.sleep(max(0, args.delay))
        except requests.RequestException as exc:
            errors.append({"url": url, "status": "erro", "erro": str(exc)[:500]})
            time.sleep(max(0, args.delay))

    output = Path(args.output)
    json_output = Path(args.json_output)
    output.parent.mkdir(parents=True, exist_ok=True)
    json_output.parent.mkdir(parents=True, exist_ok=True)
    rows = sorted(found_products.values(), key=lambda r: (r["categoria"].lower(), r["nome"].lower(), r["url_produto"]))
    with output.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=COLUMNS)
        writer.writeheader()
        writer.writerows(rows)
    result = {
        "fonte": BASE, "capturado_em_utc": started,
        "paginas_visitadas": len(visited), "paginas_html_lidas": pages_ok,
        "produtos_distintos": len(rows), "max_pages": args.max_pages,
        "atraso_segundos": args.delay,
        "observacao": "A captura cobre apenas URLs públicas permitidas pelo robots.txt e alcançáveis a partir do ponto inicial; não prova que o catálogo completo do fornecedor foi obtido. Áreas B2B/login e produtos sem metadados legíveis podem não aparecer.",
        "produtos": rows, "erros_ou_restricoes": errors,
    }
    json_output.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps({k: result[k] for k in ("fonte", "paginas_visitadas", "paginas_html_lidas", "produtos_distintos", "max_pages", "erros_ou_restricoes")}, ensure_ascii=False, indent=2))
    print(f"CSV: {output}\nJSON: {json_output}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
