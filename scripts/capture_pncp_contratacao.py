#!/usr/bin/env python3
"""Extrai uma contratação PNCP específica, incluindo dados gerais, itens e eventos.
Uso:
  python scripts/capture_pncp_contratacao.py
  python scripts/capture_pncp_contratacao.py --url https://pncp.gov.br/app/editais/00394502000144/2026/14259
Saídas em EDITAIS/CONTRATACAO-00394502000144-2026-14259/: JSON bruto, CSV e XLSX.
"""
from __future__ import annotations
import argparse, csv, json, logging, re, time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from urllib.parse import urlparse
import requests

DEFAULT_URL = "https://pncp.gov.br/app/editais/00394502000144/2026/14259"
API_ROOT = "https://pncp.gov.br/api/consulta/v1"
USER_AGENT = "LICITACAO-PNCP-Contratacao/1.0 (+https://github.com/carlos-andrade/LICITACAO)"
TIMEOUT = 40
HEADERS = ["numero_item","descricao_resumida","descricao_detalhada","quantidade","unidade","valor_unitario_estimado","valor_total_estimado","situacao_item","criterio_julgamento","link_item"]
def clean(x: Any) -> str:
    if x is None: return ""
    if isinstance(x,(dict,list)): return json.dumps(x,ensure_ascii=False,sort_keys=True)
    return re.sub(r"\s+"," ",str(x)).strip()
def pick(d: dict,*keys,default=""):
    for k in keys:
        v=d.get(k)
        if v not in (None,"",[],{}): return v
    return default
def sub(d: dict,key: str) -> dict:
    x=d.get(key,{})
    return x if isinstance(x,dict) else {}
def control_id(cnpj: str, year: int, seq: int) -> str:
    return f"{cnpj}-{year}-{seq}"
def fetch_json(session: requests.Session, url: str, params: dict|None=None) -> Any:
    last=None
    for n in range(5):
        try:
            r=session.get(url,params=params,timeout=TIMEOUT)
            if r.status_code in (429,500,502,503,504): raise requests.HTTPError(f"HTTP {r.status_code}")
            r.raise_for_status()
            payload = r.json()
            if isinstance(payload, dict) and (payload.get("error") or str(payload.get("status", "")).startswith(("301", "302", "400", "404", "500")) or "endpoint foi movido" in str(payload.get("message", "")).lower()):
                raise RuntimeError(f"Resposta de erro da API: {payload}")
            return payload
        except (requests.RequestException,ValueError) as e:
            last=e
            if n<4: time.sleep(min(2**n,20))
    raise RuntimeError(f"Não foi possível consultar {url}: {last}")
def get_data(payload: Any) -> Any:
    if isinstance(payload,dict):
        for k in ("data","resultado","content","items","contratacao","compra","dados"):
            if k in payload and isinstance(payload[k],(dict,list)): return payload[k]
    return payload
def list_data(payload: Any) -> list[dict]:
    x=get_data(payload)
    if isinstance(x,list): return [i for i in x if isinstance(i,dict)]
    if isinstance(x,dict):
        for k,v in x.items():
            if isinstance(v,list) and (not v or isinstance(v[0],dict)): return [i for i in v if isinstance(i,dict)]
    return []
def first_dict(payload: Any) -> dict:
    x=get_data(payload)
    if isinstance(x,list): return x[0] if x and isinstance(x[0],dict) else {}
    return x if isinstance(x,dict) else {}
def money(x: Any) -> str:
    if x in (None,""): return ""
    try: return f"{float(x):.2f}".replace(".",",")
    except (TypeError,ValueError): return clean(x)
def date_br(x: Any) -> str:
    if not x: return ""
    return clean(x)
def flatten_general(d: dict, captured: str, url: str, cnpj: str, year: int, seq: int) -> dict[str,str]:
    org=sub(d,"orgaoEntidade") or sub(d,"orgao")
    unit=sub(d,"unidadeOrgao") or sub(d,"unidadeCompradora")
    suborg=sub(d,"orgaoSubRogado") or sub(d,"orgaoSubrogado")
    subunit=sub(d,"unidadeSubRogada") or sub(d,"unidadeSubrogada")
    legal=sub(d,"amparoLegal")
    return {
      "url_contratacao":url,
      "titulo_aviso":clean(pick(d,"titulo","nomeCompra","objetoCompra","descricao")),
      "numero_aviso":clean(pick(d,"numeroCompra","numeroAviso","sequencialCompra",default=seq)),
      "ultima_atualizacao":clean(pick(d,"dataAtualizacao","dataAtualizacaoGlobal","dataPublicacaoPncp")),
      "orgao_cnpj":clean(pick(org,"cnpj",default=pick(d,"cnpjOrgao",default=cnpj))),
      "orgao_entidade":clean(pick(org,"razaoSocial","nome","nomeOrgao",default=pick(d,"nomeOrgao"))),
      "unidade_codigo":clean(pick(unit,"codigoUnidade","codigo","codigoUnidadeAdministrativa")),
      "unidade_compradora":clean(pick(unit,"nomeUnidade","nome","unidadeNome")),
      "uf":clean(pick(unit,"uf",default=pick(d,"uf"))),
      "municipio":clean(pick(unit,"municipioNome","nomeMunicipio",default=pick(d,"municipioNome","municipio"))),
      "orgao_subrogado":clean(pick(suborg,"razaoSocial","nome",default=pick(d,"orgaoSubRogadoNome","orgaoSubrogadoNome"))),
      "unidade_subrogada":clean(pick(subunit,"nomeUnidade","nome",default=pick(d,"unidadeSubRogadaNome","unidadeSubrogadaNome"))),
      "localidade_subrogada":clean(pick(d,"localidadeUnidadeSubRogada","localidadeSubrogada")),
      "modalidade":clean(pick(d,"modalidadeNome","nomeModalidade","modalidade")),
      "amparo_legal":clean(pick(legal,"descricao","nome",default=pick(d,"amparoLegalNome"))),
      "tipo":clean(pick(d,"tipoInstrumentoConvocatorioNome","tipoNome","tipo")),
      "modo_disputa":clean(pick(d,"modoDisputaNome","modoDisputaId")),
      "registro_preco":clean(pick(d,"srp","registroPreco")),
      "fonte_orcamentaria":clean(pick(d,"fonteOrcamentaria","orcamentoFonte")),
      "data_divulgacao_pncp":clean(pick(d,"dataPublicacaoPncp","dataPublicacao")),
      "situacao":clean(pick(d,"situacaoCompraNome","situacaoNome","situacaoCompraId")),
      "inicio_recebimento_propostas":clean(pick(d,"dataAberturaProposta","dataInicioRecebimentoPropostas")),
      "fim_recebimento_propostas":clean(pick(d,"dataEncerramentoProposta","dataFimRecebimentoPropostas")),
      "id_contratacao_pncp":clean(pick(d,"numeroControlePNCP","numeroControlePncp",default=f"{cnpj}-1-{seq:06d}/{year}")),
      "fonte":clean(pick(d,"nomeSistema","nomeUsuario","usuarioNome","fonte")),
      "objeto":clean(pick(d,"objetoCompra","objeto")),
      "informacao_complementar":clean(pick(d,"informacaoComplementar","informacaoAdicional")),
      "valor_total_estimado":money(pick(d,"valorTotalEstimado","valorTotalEstimadoCompra")),
      "valor_total_homologado":money(pick(d,"valorTotalHomologado")),
      "capturado_em_utc":captured,
    }
def flatten_item(item: dict, fallback_num: int) -> dict[str,str]:
    unit=sub(item,"unidadeMedida") or sub(item,"unidade")
    return {
      "numero_item":clean(pick(item,"numeroItem","itemNumero","sequencialItem",default=fallback_num)),
      "descricao_resumida":clean(pick(item,"descricao","descricaoItem","nome")),
      "descricao_detalhada":clean(pick(item,"descricaoDetalhada","descricaoComplementar","especificacao")),
      "quantidade":clean(pick(item,"quantidade","quantidadeItem")),
      "unidade":clean(pick(unit,"nome","sigla",default=pick(item,"unidadeMedidaNome","unidadeFornecimento"))),
      "valor_unitario_estimado":money(pick(item,"valorUnitarioEstimado","valorUnitario")),
      "valor_total_estimado":money(pick(item,"valorTotal","valorTotalEstimado")),
      "situacao_item":clean(pick(item,"situacaoCompraItemNome","situacaoItem","situacao")),
      "criterio_julgamento":clean(pick(item,"criterioJulgamentoNome","criterioJulgamento")),
      "link_item":clean(pick(item,"link","uri")),
    }
def flatten_event(e: dict) -> dict[str,str]:
    return {k:clean(v) for k,v in {
      "data":pick(e,"logManutencaoDataInclusao","data","dataEvento","dataHora"),
      "tipo":pick(e,"tipoLogManutencaoNome","tipo","tipoEvento","descricaoTipoEvento"),
      "descricao":pick(e,"justificativa","descricao","descricaoEvento","mensagem","documentoTitulo"),
      "usuario":pick(e,"usuarioNome","usuario","nomeUsuario"),
    }.items()}
def write_csv(path: Path, rows: list[dict], fields: list[str]) -> None:
    with path.open("w",encoding="utf-8-sig",newline="") as f:
        w=csv.DictWriter(f,fieldnames=fields,delimiter=";",extrasaction="ignore")
        w.writeheader(); w.writerows(rows)
def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--url",default=DEFAULT_URL)
    p.add_argument("--output-dir",default="")
    p.add_argument("--no-items",action="store_true")
    args=p.parse_args()
    parsed=urlparse(args.url)
    m=re.fullmatch(r"/app/editais/(\d{14})/(\d{4})/(\d+)",parsed.path)
    if parsed.hostname not in ("pncp.gov.br","www.pncp.gov.br") or not m:
        p.error("URL inválida: use https://pncp.gov.br/app/editais/{CNPJ}/{ANO}/{SEQUENCIAL}")
    cnpj,year_s,seq_s=m.groups(); year=int(year_s); seq=int(seq_s)
    out=Path(args.output_dir) if args.output_dir else Path("EDITAIS")/f"CONTRATACAO-{cnpj}-{year}-{seq}"
    out.mkdir(parents=True,exist_ok=True)
    s=requests.Session(); s.headers.update({"Accept":"application/json","User-Agent":USER_AGENT})
    captured=datetime.now(timezone.utc).isoformat(timespec="seconds")
    # Endpoints documented by PNCP: public contracting details, items and events.
    candidates=[
      ("geral",f"{API_ROOT}/orgaos/{cnpj}/compras/{year}/{seq}",None),
      ("itens",f"{API_ROOT}/orgaos/{cnpj}/compras/{year}/{seq}/itens",{"pagina":1,"tamanhoPagina":100}),
      ("eventos",f"{API_ROOT}/orgaos/{cnpj}/compras/{year}/{seq}/historico",None),
    ]
    raw={}; errors={}
    for key,endpoint,params in candidates:
      if key=="itens" and args.no_items: continue
      try: raw[key]=fetch_json(s,endpoint,params)
      except Exception as e: errors[key]=str(e); logging.warning("%s: %s",key,e)
    general=first_dict(raw.get("geral",{}))
    items=list_data(raw.get("itens",{}))
    events=list_data(raw.get("eventos",{}))
    general_row=flatten_general(general,captured,args.url,cnpj,year,seq)
    item_rows=[flatten_item(it,i+1) for i,it in enumerate(items)]
    event_rows=[flatten_event(e) for e in events]
    meta={
      "status":"COMPLETO" if "geral" in raw and "itens" in raw and general and len(items) > 0 and not errors else ("PARCIAL" if raw else "FALHA"),
      "capturado_em_utc":captured,"url_contratacao":args.url,"cnpj":cnpj,"ano":year,"sequencial":seq,
      "endpoints_consultados":[x[1] for x in candidates],
      "base_api":"https://pncp.gov.br/api/pncp",
      "documentacao_api":"https://pncp.gov.br/manual/pt-br/latest/contratacao/consultar_historico_da_contratacao.html","erros_por_endpoint":errors,
      "quantidade_itens":len(item_rows),"quantidade_eventos":len(event_rows),
      "observacao":"Os campos são preenchidos com os valores efetivamente devolvidos pela API; campos ausentes permanecem vazios. A extração deve ser comparada à página pública se o PNCP alterar o esquema dos endpoints."
    }
    (out/"contratacao-geral.json").write_text(json.dumps(raw.get("geral",{}),ensure_ascii=False,indent=2),encoding="utf-8")
    (out/"itens.json").write_text(json.dumps(raw.get("itens",{}),ensure_ascii=False,indent=2),encoding="utf-8")
    (out/"eventos.json").write_text(json.dumps(raw.get("eventos",{}),ensure_ascii=False,indent=2),encoding="utf-8")
    (out/"metadados.json").write_text(json.dumps(meta,ensure_ascii=False,indent=2),encoding="utf-8")
    write_csv(out/"contratacao-geral.csv",[general_row],list(general_row.keys()))
    write_csv(out/"itens.csv",item_rows,HEADERS)
    write_csv(out/"historico.csv",event_rows,["data","tipo","descricao","usuario"])
    try:
      from openpyxl import Workbook
      from openpyxl.styles import Alignment,Font,PatternFill
      from openpyxl.utils import get_column_letter
      wb=Workbook(); ws=wb.active; ws.title="Dados gerais"
      ws.append(list(general_row.keys())); ws.append(list(general_row.values()))
      for c in ws[1]:
        c.font=Font(color="FFFFFF",bold=True); c.fill=PatternFill("solid",fgColor="17365D"); c.alignment=Alignment(wrap_text=True)
      ws.freeze_panes="A2"; ws.auto_filter.ref=ws.dimensions
      wi=wb.create_sheet("Itens"); wi.append(HEADERS)
      for row in item_rows: wi.append([row.get(k,"") for k in HEADERS])
      for c in wi[1]:
        c.font=Font(color="FFFFFF",bold=True); c.fill=PatternFill("solid",fgColor="17365D"); c.alignment=Alignment(wrap_text=True)
      wi.freeze_panes="A2"; wi.auto_filter.ref=wi.dimensions
      wh=wb.create_sheet("Histórico"); histcols=["data","tipo","descricao","usuario"]; wh.append(histcols)
      for row in event_rows: wh.append([row.get(k,"") for k in histcols])
      for c in wh[1]:
        c.font=Font(color="FFFFFF",bold=True); c.fill=PatternFill("solid",fgColor="17365D")
      wh.freeze_panes="A2"; wh.auto_filter.ref=wh.dimensions
      wm=wb.create_sheet("Metadados"); wm.append(["campo","valor"])
      for k,v in meta.items(): wm.append([k,json.dumps(v,ensure_ascii=False) if isinstance(v,(dict,list)) else str(v)])
      for col in range(1,wm.max_column+1): wm.column_dimensions[get_column_letter(col)].width=42
      for sheet in wb.worksheets:
        sheet.sheet_view.showGridLines=False
        for col in range(1,sheet.max_column+1):
          longest=max([len(str(sheet.cell(r,col).value or "")) for r in range(1,min(sheet.max_row,200)+1)] or [12])
          sheet.column_dimensions[get_column_letter(col)].width=min(max(longest+2,12),55)
      wb.save(out/"contratacao-completa.xlsx")
    except ImportError: logging.warning("openpyxl não instalado; CSV e JSON gerados.")
    print(json.dumps({"status":meta["status"],"diretorio":str(out),"campos_gerais":len(general_row),"itens":len(item_rows),"eventos":len(event_rows),"erros":errors},ensure_ascii=False,indent=2))
    return 0 if meta["status"] == "COMPLETO" else 2
if __name__=="__main__": raise SystemExit(main())
