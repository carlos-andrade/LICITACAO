#!/usr/bin/env python3
"""Captura catálogo ALLNATIONS com login opcional por secrets do ambiente.

Uso:
  python scripts/capture_allnations_catalog.py
  python scripts/capture_allnations_catalog.py --output FORNECEDORES/allnations-produtos.csv
  python scripts/capture_allnations_catalog.py --max-pages 150 --delay 1.5

A autenticação opcional usa ALLNATIONS_EMAIL e ALLNATIONS_PASSWORD via ambiente.
Não grava credenciais ou cookies nos resultados e não contorna CAPTCHA/MFA.
Respeita robots.txt; preços ausentes não são inventados.
"""
from __future__ import annotations

import argparse
import csv
import json
import os
import re
import sys
import time
import urllib.robotparser
from collections import deque
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from xml.etree import ElementTree
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
    "categoria", "preco", "moeda", "disponibilidade", "quantidade_estoque", "url_produto",
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

def stock_from_product(p: dict[str, Any]) -> str:
    """Retorna quantidade apenas quando o catálogo fornece número explícito."""
    offers = p.get("offers")
    if isinstance(offers, list):
        offers = offers[0] if offers else {}
    offers = offers if isinstance(offers, dict) else {}
    for node in (p, offers, offers.get("inventoryLevel")):
        if not isinstance(node, dict):
            continue
        for key in ("inventoryLevel", "quantity", "inventoryQuantity", "stock", "stockQuantity", "availableQuantity"):
            value = node.get(key)
            if isinstance(value, dict):
                value = value.get("value")
            if value is not None and re.fullmatch(r"\s*\d+(?:\.0+)?\s*", str(value)):
                return str(int(float(value)))
    return ""

def _explicit_quantity(value: Any) -> str:
    """Normaliza apenas números inteiros explícitos; não converte disponibilidade em quantidade."""
    if isinstance(value, dict):
        # Schema.org QuantitativeValue: {"value": 12, "unitCode": "C62"}
        value = value.get("value")
    if isinstance(value, bool) or value is None:
        return ""
    raw = str(value).strip()
    if re.fullmatch(r"\d+(?:\.0+)?", raw):
        return str(int(float(raw)))
    return ""


def _quantity_in_object(node: Any, depth: int = 0) -> str:
    """Procura campos de quantidade conhecidos em estruturas JSON embutidas, com profundidade limitada."""
    if depth > 12:
        return ""
    if isinstance(node, dict):
        # Only accept quantity-specific keys; generic "value" is accepted only inside a quantity field.
        keys = (
            "inventoryLevel", "inventoryQuantity", "stockQuantity",
            "availableQuantity", "quantityAvailable", "quantityInStock",
            "stock_quantity", "inventory_quantity", "stock_quantity_value",
            "qtyAvailable", "qty_available", "quantity",
        )
        for key in keys:
            if key in node:
                result = _explicit_quantity(node[key])
                if result:
                    return result
        # Recurse into common product/offer/state containers, avoiding arbitrary unrelated page values.
        for key in ("product", "products", "item", "items", "offer", "offers", "inventory", "stock", "data", "props", "pageProps", "productData", "variants", "variant"):
            if key in node:
                result = _quantity_in_object(node[key], depth + 1)
                if result:
                    return result
        return ""
    if isinstance(node, list):
        for item in node[:200]:
            result = _quantity_in_object(item, depth + 1)
            if result:
                return result
    return ""


def visible_stock_quantity(soup: BeautifulSoup) -> str:
    """Extrai quantidade numérica explícita de HTML, atributos e JSON embutido."""
    selectors = (
        '[itemprop="inventoryLevel"]', '[itemprop="inventoryQuantity"]',
        '[itemprop="quantity"]', '[data-stock-quantity]', '[data-inventory-quantity]',
        '[data-quantity]', '[data-stock]', '.stock-quantity', '.stockQuantity',
        '.inventory-quantity', '.available-quantity', '.qty-available',
        '[data-testid*="stock" i]', '[data-testid*="quantity" i]',
        '[class*="stock-quantity" i]', '[class*="inventory-quantity" i]',
        '[class*="available-quantity" i]',
    )
    for selector in selectors:
        for tag in soup.select(selector)[:10]:
            value = text(tag.get("content") or tag.get("value") or
                         tag.get("data-stock-quantity") or tag.get("data-inventory-quantity") or
                         tag.get("data-quantity") or tag.get("data-stock") or
                         tag.get_text(" ", strip=True))
            match = re.fullmatch(r"\s*(?:quantidade\s*(?:em estoque)?\s*:?\s*)?(\d+)\s*(?:unidades?|pcs?)?\s*", value, re.I)
            if match:
                return match.group(1)

    # Product pages may embed inventory in application/json or framework state rather than JSON-LD.
    for tag in soup.find_all("script"):
        raw = tag.string or tag.get_text()
        if not raw or len(raw) > 2_000_000:
            continue
        script_type = (tag.get("type") or "").lower()
        script_id = (tag.get("id") or "").lower()
        if "json" in script_type or script_id in ("__next_data__", "__nuxt_data__"):
            try:
                quantity = _quantity_in_object(json.loads(raw))
                if quantity:
                    return quantity
            except (ValueError, TypeError):
                pass

    # Last resort: numeric quantity only inside elements whose labels explicitly mention stock/quantity.
    for tag in soup.select('[aria-label*="estoque" i], [aria-label*="quantidade" i], [title*="estoque" i], [title*="quantidade" i]')[:20]:
        value = text(tag.get("aria-label") or tag.get("title") or tag.get_text(" ", strip=True))
        match = re.fullmatch(r"\s*(?:quantidade\s*(?:em estoque)?\s*:?\s*)?(\d+)\s*(?:unidades?|pcs?)?\s*", value, re.I)
        if match:
            return match.group(1)
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
    stock_quantity = stock_from_product(p) or visible_stock_quantity(soup)
    # Fallback only to explicit product-price metadata in the same product page.
    if not price:
        price_tag = soup.select_one('meta[property="product:price:amount"], meta[itemprop="price"], [itemprop="price"]')
        if price_tag:
            price = text(price_tag.get("content") or price_tag.get("value") or price_tag.get_text(" ", strip=True))
    if not currency:
        currency_tag = soup.select_one('meta[property="product:price:currency"], meta[itemprop="priceCurrency"], [itemprop="priceCurrency"]')
        if currency_tag:
            currency = text(currency_tag.get("content") or currency_tag.get("value") or currency_tag.get_text(" ", strip=True))
    price_source = "JSON-LD/Product" if price else ""
    if not price:
        price, price_source = extract_visible_price(soup)
    if price and not currency:
        currency = "BRL"
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
        "quantidade_estoque": stock_quantity,
        "url_produto": url,
        "origem_dado": price_source or "JSON-LD/Product",
        "status_captura": "capturado_com_preco" if price else "produto_sem_preco_exposto",
        "observacoes": "Preço capturado apenas quando explicitamente exposto; validar condições comerciais.",
    }


def login_with_env(session: requests.Session, robots: urllib.robotparser.RobotFileParser,
                   timeout: float) -> tuple[bool, str]:
    """Login opcional por formulário HTML convencional, sem expor credenciais."""
    email = os.environ.get("ALLNATIONS_EMAIL", "").strip()
    password = os.environ.get("ALLNATIONS_PASSWORD", "")
    if not email and not password:
        return False, "secrets de login não configurados; modo público"
    if not email or not password:
        return False, "configuração incompleta: defina ALLNATIONS_EMAIL e ALLNATIONS_PASSWORD"
    login_url = urljoin(BASE, "login")
    try:
        if not robots.can_fetch(USER_AGENT, login_url) or not robots.can_fetch("*", login_url):
            return False, "robots.txt não permite abrir a URL de login"
        response = session.get(login_url, timeout=timeout)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        form = next((f for f in soup.find_all("form") if f.select_one('input[type="password"]')), None)
        if form is None:
            return False, "formulário de login convencional não identificado"
        password_input = form.select_one('input[type="password"]')
        email_input = form.select_one('input[type="email"], input[name*="email" i], input[name*="username" i], input[name*="login" i]')
        if not email_input or not email_input.get("name") or not password_input.get("name"):
            return False, "campos de e-mail/senha não identificados"
        payload = {}
        for field in form.select("input[name]"):
            kind = (field.get("type") or "text").lower()
            if kind == "hidden":
                payload[field["name"]] = field.get("value", "")
            elif kind in ("checkbox", "radio") and field.has_attr("checked"):
                payload[field["name"]] = field.get("value", "on")
        payload[email_input["name"]] = email
        payload[password_input["name"]] = password
        action = urljoin(response.url, form.get("action") or response.url)
        parsed = urlparse(action)
        if parsed.scheme != "https" or parsed.hostname not in (DOMAIN, "www." + DOMAIN):
            return False, "ação de login fora do domínio HTTPS esperado"
        submitted = session.post(action, data=payload, timeout=timeout, allow_redirects=True)
        submitted.raise_for_status()
        result_soup = BeautifulSoup(submitted.text, "html.parser")
        if result_soup.select_one('input[type="password"]'):
            return False, "login não confirmado; formulário de senha continua presente"
        page_text = result_soup.get_text(" ", strip=True).lower()
        authenticated_markers = ("sair", "logout", "minha conta", "my account", "log out")
        if not any(marker in page_text for marker in authenticated_markers):
            return False, "login não confirmado por indicador de sessão; sem captura autenticada"
        return True, "sessão autenticada confirmada por indicador da página"
    except requests.RequestException as exc:
        return False, "falha de rede no login: " + type(exc).__name__

def extract_visible_price(soup: BeautifulSoup) -> tuple[str, str]:
    """Extrai preço somente de campos/seletores explícitos de preço."""
    selectors = (
        'meta[property="product:price:amount"]',
        'meta[itemprop="price"]',
        '[itemprop="price"][content]',
        '[itemprop="price"][value]',
        '.product-price .price',
        '.prices .actual-price',
        '.actual-price',
        '.price-value',
        '.product-price',
    )
    for selector in selectors:
        tag = soup.select_one(selector)
        if not tag:
            continue
        value = text(tag.get("content") or tag.get("value") or tag.get_text(" ", strip=True))
        if re.search(r"\d", value) and re.fullmatch(r"[\sR$€£A-Z]*\d[\d.,\s]*", value, re.I):
            return value.strip(), "HTML/preço-visível"
    return "", ""

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
    price = meta("product:price:amount")
    currency = meta("product:price:currency")
    stock_quantity = visible_stock_quantity(soup)
    price_source = "Open Graph/meta" if price else ""
    if not price:
        price, price_source = extract_visible_price(soup)
    if price and not currency:
        currency = "BRL"
    return {
        "capturado_em_utc": timestamp, "nome": name,
        "marca": meta("product:brand"), "modelo": meta("product:retailer_item_id"),
        "sku": meta("product:retailer_item_id"), "gtin": "",
        "categoria": "", "preco": price,
        "moeda": currency,
        "disponibilidade": meta("product:availability"),
        "quantidade_estoque": stock_quantity,
        "url_produto": url, "origem_dado": price_source or "Open Graph/meta",
        "status_captura": "capturado_com_preco" if price else "produto_sem_preco_exposto",
        "observacoes": "Preço não inferido; confirmar condições comerciais quando ausente.",
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

    auth_ok, auth_status = login_with_env(session, robots, args.timeout)
    print("Autenticacao ALLNATIONS: " + auth_status)
    if not auth_ok and (os.environ.get("ALLNATIONS_EMAIL") or os.environ.get("ALLNATIONS_PASSWORD")):
        print("Erro: login não confirmado; encerrando para evitar publicar captura pública como autenticada.", file=sys.stderr)
        return 4

    if not allowed(start):
        print(f"robots.txt não permite capturar {start}. Encerrado sem contornar a regra.", file=sys.stderr)
        return 3

    queue = deque([start])
    errors: list[dict[str, str]] = []
    # Discover public sitemap URLs where permitted, to improve catalog coverage.
    sitemap_candidates = [urljoin(BASE, "/sitemap.xml"), urljoin(BASE, "/sitemap_index.xml")]
    for sitemap_url in sitemap_candidates:
        if not allowed(sitemap_url):
            continue
        try:
            sitemap_response = session.get(sitemap_url, timeout=args.timeout)
            if sitemap_response.ok and "xml" in sitemap_response.headers.get("Content-Type", "").lower():
                # Parse XML with the standard library; no optional lxml dependency required.
                root = ElementTree.fromstring(sitemap_response.content)
                for loc in root.iter():
                    if loc.tag.rsplit("}", 1)[-1].lower() == "loc" and loc.text:
                        candidate = normalize_url(loc.text.strip())
                        if candidate and candidate not in queue:
                            queue.append(candidate)
        except requests.RequestException as exc:
            errors.append({"url": sitemap_url, "status": "erro_sitemap", "erro": str(exc)[:300]})
    visited: set[str] = set()
    found_products: dict[str, dict[str, str]] = {}
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
        "modo_autenticacao": "autenticado" if auth_ok else "publico_ou_login_nao_confirmado",
        "status_autenticacao": auth_status,
        "precos_capturados": sum(1 for row in rows if row.get("preco")),
        "produtos_sem_preco": sum(1 for row in rows if not row.get("preco")),
        "quantidades_estoque_capturadas": sum(1 for row in rows if row.get("quantidade_estoque") != ""),
        "produtos_sem_quantidade_estoque_exposta": sum(1 for row in rows if row.get("quantidade_estoque") == ""),
        "observacao": "A captura respeita robots.txt e não contorna CAPTCHA/MFA. Preços ausentes não são inferidos.",
        "produtos": rows, "erros_ou_restricoes": errors,
    }
    json_output.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps({k: result[k] for k in ("fonte", "paginas_visitadas", "paginas_html_lidas", "produtos_distintos", "precos_capturados", "produtos_sem_preco", "quantidades_estoque_capturadas", "produtos_sem_quantidade_estoque_exposta", "max_pages", "erros_ou_restricoes")}, ensure_ascii=False, indent=2))
    print(f"CSV: {output}\nJSON: {json_output}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
