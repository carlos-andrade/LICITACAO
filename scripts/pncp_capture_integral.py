#!/usr/bin/env python3
"""PNCP full-page/network capture. Install: pip install requests beautifulsoup4 playwright; python -m playwright install chromium"""
import argparse,csv,json,re,sys,hashlib
from pathlib import Path
from datetime import datetime
from urllib.parse import urlparse
import requests
API="https://pncp.gov.br/api/consulta/v1"
S=requests.Session(); S.headers.update({"User-Agent":"LICITACAO-PNCP-Capture/2.0","Accept":"application/json, text/html, */*"})
def fetch(u):
 try:
  r=S.get(u,timeout=35); meta={"url":u,"http":r.status_code,"type":r.headers.get("content-type","")}
  if not r.ok: meta["error"]=r.text[:300]; return None,meta
  try: return r.json(),meta
  except ValueError: return r.text,meta
 except Exception as e: return None,{"url":u,"error":str(e)}
def flat(x,p=""):
 out=[]
 if isinstance(x,dict):
  for k,v in x.items():
   q=f"{p}.{k}" if p else str(k); out.extend(flat(v,q) if isinstance(v,(dict,list)) else [(q,v)])
 elif isinstance(x,list):
  for i,v in enumerate(x): out.extend(flat(v,f"{p}[{i}]"))
 else: out.append((p,x))
 return out
def main():
 ap=argparse.ArgumentParser(); ap.add_argument("url"); ap.add_argument("--output-dir",default="EDITAIS"); ap.add_argument("--download-files",action="store_true"); a=ap.parse_args()
 p=urlparse(a.url); m=re.search(r"/app/editais/(\d{14})/(\d{4})/(\d+)",p.path)
 if p.hostname not in ("pncp.gov.br","www.pncp.gov.br") or not m: raise ValueError("URL PNCP não reconhecida")
 cnpj,year,seq=m.groups(); out=Path(a.output_dir); out.mkdir(parents=True,exist_ok=True); stamp=datetime.now().astimezone().isoformat()
 root=f"{API}/orgaos/{cnpj}/compras/{year}/{seq}"
 urls=[root]+[root+"/"+x for x in ("itens","arquivos","historico","atas","contratos","empenhos")]
 diagnostics=[]; data=[]
 for u in urls:
  x,d=fetch(u); diagnostics.append(d)
  if x is not None: data.append({"url":u,"data":x})
 browser={"available":False,"html":"","text":"","links":[],"frames":[],"responses":[],"errors":[]}
 try:
  from playwright.sync_api import sync_playwright
  with sync_playwright() as pw:
   b=pw.chromium.launch(headless=True); page=b.new_page()
   def response(r):
    try:
     ct=r.headers.get("content-type","")
     if "json" in ct or "/api/" in r.url:
      z={"url":r.url,"http":r.status,"type":ct}
      try:
       if "json" in ct:z["body"]=r.json()
       elif r.status<400:z["text"]=r.text()[:500000]
      except Exception as e:z["error"]=str(e)
      browser["responses"].append(z)
    except Exception: pass
   page.on("response",response)
   try: page.goto(a.url,wait_until="domcontentloaded",timeout=90000)
   except Exception as e: browser["errors"].append(str(e))
   try: page.wait_for_load_state("networkidle",timeout=20000)
   except Exception: pass
   for _ in range(4):
    try: page.mouse.wheel(0,1600); page.wait_for_timeout(500)
    except Exception: break
   # Click tabs to trigger lazy loading of the requested sections.
   try:
    tabs=page.get_by_role("tab")
    for i in range(min(tabs.count(),30)):
     t=tabs.nth(i)
     try:
      label=(t.inner_text(timeout=500) or "").lower()
      if any(k in label for k in ("item","arquivo","document","ata","contrato","empenho","histórico","historico")): t.click(timeout=1200); page.wait_for_timeout(500)
     except Exception: pass
   except Exception: pass
   browser["available"]=True; browser["html"]=page.content()[:5000000]; browser["text"]=page.locator("body").inner_text()[:1000000]
   browser["links"]=page.locator("a").evaluate_all("(a)=>a.map(x=>({text:(x.innerText||'').trim(),url:x.href})).filter(x=>x.url)")
   browser["frames"]=[{"url":f.url,"name":f.name} for f in page.frames]; b.close()
 except ImportError: browser["errors"].append("Playwright ausente; instale playwright e Chromium.")
 except Exception as e: browser["errors"].append(str(e))
 for r in browser["responses"]:
  if "body" in r:data.append({"url":r["url"],"data":r["body"],"source":"browser-network"})
 files=[]; seen=set()
 for d in data:
  for k,v in flat(d.get("data")):
   if isinstance(v,str) and v.startswith("http") and any(t in k.lower() for t in ("url","arquivo","documento","anexo","link")) and v not in seen:
    seen.add(v); files.append({"url":v,"source":d["url"],"field":k})
 for l in browser["links"]:
  if l["url"].startswith("http") and l["url"] not in seen: seen.add(l["url"]); files.append({"url":l["url"],"source":"rendered-page","field":l["text"]})
 downloads=[]
 if a.download_files:
  folder=out/f"{year}-{seq}-{cnpj}_arquivos"; folder.mkdir(exist_ok=True)
  for i,f in enumerate(files,1):
   try:
    with S.get(f["url"],stream=True,timeout=35) as r:
     if not r.ok: downloads.append({"url":f["url"],"status":f"HTTP {r.status_code}"}); continue
     dest=folder/f"{i:03d}-{Path(urlparse(f['url']).path).name or 'arquivo.bin'}"; h=hashlib.sha256(); n=0
     with dest.open("wb") as w:
      for chunk in r.iter_content(131072):
       if chunk:
        n+=len(chunk)
        if n>150*1024*1024: raise ValueError("arquivo excedeu 150 MB")
        w.write(chunk); h.update(chunk)
     downloads.append({"url":f["url"],"status":"baixado","path":str(dest),"bytes":n,"sha256":h.hexdigest()})
   except Exception as e: downloads.append({"url":f["url"],"status":str(e)})
 raw={"url":a.url,"captured_at":stamp,"id":{"cnpj":cnpj,"year":year,"sequence":seq},"diagnostics":diagnostics,"api_responses":data,"browser":browser,"files":files,"downloads":downloads}
 stem=f"{year}-{seq}-{cnpj}"; jp=out/f"{stem}-captura-integral.json"; jp.write_text(json.dumps(raw,ensure_ascii=False,indent=2),encoding="utf-8")
 cp=out/f"{stem}-todos-campos.csv"
 with cp.open("w",newline="",encoding="utf-8-sig") as f:
  w=csv.DictWriter(f,fieldnames=["endpoint","campo","valor"]); w.writeheader()
  for d in data:
   for k,v in flat(d.get("data")): w.writerow({"endpoint":d["url"],"campo":k,"valor":json.dumps(v,ensure_ascii=False) if isinstance(v,(dict,list)) else str(v)})
 sections={"Itens":("item",),"Arquivos":("arquivo","document","anexo"),"Atas de Registro de Preço":("ata","registro-preco","registropreco"),"Contratos/Empenhos":("contrato","empenho"),"Histórico":("histor","evento","timeline")}
 md=[f"# Captura integral PNCP {cnpj}/{year}/{seq}","",f"- URL: {a.url}",f"- Data: {stamp}",f"- JSON bruto: {jp.name}",f"- CSV com todos os campos: {cp.name}",f"- Playwright ativo: {browser['available']}",f"- Respostas API/rede: {len(data)}",f"- Links/arquivos detectados: {len(files)}","","## Diagnóstico","","| URL | HTTP | Erro |","|---|---:|---|"]
 for d in diagnostics: md.append(f"| {d.get('url','')} | {d.get('http','—')} | {d.get('error','')} |")
 md+=["","## Cobertura por seção","","| Seção | Endpoints encontrados |","|---|---|"]
 for name,terms in sections.items():
  hits=sorted(set(d["url"] for d in data if any(t in d["url"].lower() for t in terms)))
  md.append(f"| {name} | {'<br>'.join(hits) if hits else 'Nenhum endpoint reconhecido; verificar JSON e diagnóstico'} |")
 md+=["","## Arquivos e links","","| Nº | URL | Origem | Campo/rótulo |","|---:|---|---|---|"]
 for i,x in enumerate(files,1): md.append(f"| {i} | {x['url']} | {x['source']} | {x['field']} |")
 md+=["","## Limitações","- Captura best-effort; respostas HTTP com erro não provam que uma seção esteja vazia.","- Verifique paginação no JSON; esta versão registra respostas capturadas mas não garante que percorra todas as páginas.","- O JSON bruto contém o texto e HTML renderizados, frames e respostas JSON observadas na rede.","- Download de anexos não equivale a extrair o conteúdo interno de PDF/Office; OCR e extração de tabelas são etapas separadas."]
 mp=out/f"{stem}-captura-integral.md"; mp.write_text("\n".join(md),encoding="utf-8")
 print("Markdown:",mp); print("JSON:",jp); print("CSV:",cp); print("Respostas:",len(data),"Arquivos:",len(files))
if __name__=="__main__":
 try: main()
 except Exception as e: print("ERRO:",e,file=sys.stderr); sys.exit(2)
