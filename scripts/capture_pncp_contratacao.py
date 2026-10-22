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
CONSULTA_ROOT = "https://pncp.gov.br/api/consulta/v1"
API_ROOT = "https://pncp.gov.br/api/pncp/v1"
PROPOSTA_URL = f"{CONSULTA_ROOT}/contratacoes/proposta"
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
    """Consulta a API sem repetir 404 determinísticos e respeitando limites temporários."""
    last=None
    for n in range(4):
        try:
            r=session.get(url,params=params,timeout=TIMEOUT)
            if r.status_code == 404:
                raise RuntimeError(f"HTTP 404 em {r.url}")
            if r.status_code == 429 or r.status_code in (500,502,503,504):
                last=f"HTTP {r.status_code} em {r.url}"
                if n < 3:
                    retry=r.headers.get("Retry-After","")
                    try: wait=max(1,min(float(retry),45)) if retry else min(2**(n+1),20)
                    except ValueError: wait=min(2**(n+1),20)
                    time.sleep(wait)
                    continue
                raise RuntimeError(last)
            r.raise_for_status()
            try:
                payload=r.json()
            except ValueError as e:
                raise RuntimeError(f"Resposta não é JSON válido em {r.url}: {e}") from e
            if isinstance(payload,dict) and (
                payload.get("error")
                or str(payload.get("status","")).startswith(("301","302","400","404","500"))
                or "endpoint foi movido" in str(payload.get("message","")).lower()
            ):
                raise RuntimeError(f"Resposta de erro da API em {r.url}: {payload}")
            return payload
        except RuntimeError:
            raise
        except requests.RequestException as e:
            last=e
            if n < 3:
                time.sleep(min(2**(n+1),20))
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
def find_open_proposal(session: requests.Session, cnpj: str, year: int, seq: int) -> tuple[dict,str]:
    """Fallback público com variações de filtro e busca de publicação."""
    from datetime import timedelta
    expected_cnpj=cnpj
    expected_year=int(year)
    expected_seq=int(seq)
    today=datetime.now(timezone.utc).date()
    future=(today+timedelta(days=365)).strftime("%Y%m%d")
    past=(today-timedelta(days=45)).strftime("%Y%m%d")
    variants=[
      # PNCP usa código 100 para Dispensa; 8 é Pré-qualificação.
      ("proposta_cnpj_dispensa",PROPOSTA_URL,{"dataFinal":future,"codigoModalidadeContratacao":100,"cnpj":cnpj,"tamanhoPagina":50},5),
      ("proposta_cnpj",PROPOSTA_URL,{"dataFinal":future,"cnpj":cnpj,"tamanhoPagina":50},3),
      ("publicacao_cnpj_dispensa",f"{CONSULTA_ROOT}/contratacoes/publicacao",{"dataInicial":past,"dataFinal":future,"codigoModalidadeContratacao":100,"cnpj":cnpj,"tamanhoPagina":50},5),
    ]
    diagnostics=[]
    for variant_name,endpoint,base_params,max_pages in variants:
        pages_scanned=0
        records_seen=0
        samples=[]
        for page in range(1,max_pages+1):
            try:
                payload=fetch_json(session,endpoint,{**base_params,"pagina":page})
            except Exception as exc:
                diagnostics.append(f"{variant_name}: falha na página {page}: {exc}")
                break
            records=list_data(payload)
            pages_scanned=page
            records_seen+=len(records)
            for record in records:
                control=clean(pick(record,"numeroControlePNCP","numeroControlePncp"))
                if len(samples)<4 and control:
                    samples.append(control)
                match=re.fullmatch(r"(\d{14})-(\d+)-(\d+)/(\d{4})",control)
                if match:
                    rec_cnpj,_,rec_seq,rec_year=match.groups()
                    if rec_cnpj==expected_cnpj and int(rec_year)==expected_year and int(rec_seq)==expected_seq:
                        return record,variant_name
            if not records or len(records)<50:
                break
            total_pages=pick(payload,"totalPaginas","totalPaginasEncontradas","pages",default="")
            try:
                if total_pages and page>=int(total_pages):
                    break
            except (ValueError,TypeError):
                pass
            time.sleep(0.3)
        diagnostics.append(f"{variant_name}: páginas={pages_scanned}; registros={records_seen}; amostras={samples}")
    raise RuntimeError(
        f"Contratação {cnpj}-1-{seq:06d}/{year} não localizada nas rotas públicas alternativas. "
        + " | ".join(diagnostics)
    )

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
      "orgao_entidade":clean(pick(org,"razaoSocial","nome","nomeOrgao",default=pick(d,"nomeOrgao","razaoSocialOrgao"))),
      "unidade_codigo":clean(pick(unit,"codigoUnidade","codigo","codigoUnidadeAdministrativa",default=pick(d,"codigoUnidadeAdministrativa"))),
      "unidade_compradora":clean(pick(unit,"nomeUnidade","nome","unidadeNome",default=pick(d,"unidadeNome","nomeUnidade"))),
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
      "unidade":clean(pick(unit,"nome","sigla",default=pick(item,"unidadeMedidaNome","unidadeFornecimento","unidadeMedida"))),
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
      "descricao":pick(e,"justificativa","descricao","descricaoEvento","mensagem","documentoTitulo","categoriaLogManutencaoNome"),
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
    # O PNCP mantém a consulta pública e a API de itens/histórico em bases distintas.
    general_endpoint=f"{CONSULTA_ROOT}/orgaos/{cnpj}/compras/{year}/{seq}"
    items_endpoint=f"{API_ROOT}/orgaos/{cnpj}/compras/{year}/{seq}/itens"
    events_endpoint=f"{API_ROOT}/orgaos/{cnpj}/compras/{year}/{seq}/historico"
    raw={}; errors={}; warnings={}; general_source="consulta_detalhe"
    try:
      raw["geral"]=fetch_json(s,general_endpoint)
    except Exception as e:
      if "404" in str(e) or "endpoint foi movido" in str(e).lower():
        warnings["geral_detalhe"]=str(e)
        try:
          raw["geral"],general_source=find_open_proposal(s,cnpj,year,seq)
        except Exception as fallback_error:
          errors["geral"]=f"Detalhe: {e}; fallback de propostas: {fallback_error}"
          logging.warning("geral: %s",errors["geral"])
      else:
        errors["geral"]=str(e)
        logging.warning("geral: %s",e)
    time.sleep(0.75)
    if not args.no_items:
      try: raw["itens"]=fetch_json(s,items_endpoint,{"pagina":1,"tamanhoPagina":100})
      except Exception as e: errors["itens"]=str(e); logging.warning("itens: %s",e)
      time.sleep(0.75)
    try: raw["eventos"]=fetch_json(s,events_endpoint,{"pagina":1,"tamanhoPagina":100})
    except Exception as e: errors["eventos"]=str(e); logging.warning("eventos: %s",e)
    general=first_dict(raw.get("geral",{}))
    items=list_data(raw.get("itens",{}))
    events=list_data(raw.get("eventos",{}))
    general_row=flatten_general(general,captured,args.url,cnpj,year,seq)
    item_rows=[flatten_item(it,i+1) for i,it in enumerate(items)]
    event_rows=[flatten_event(e) for e in events]
    expected_items=(len(item_rows)==14) if not args.no_items else False
    general_is_error = isinstance(raw.get("geral"), dict) and bool(raw.get("geral", {}).get("error"))
    items_have_units = bool(item_rows) and all(row.get("unidade") for row in item_rows)
    events_have_data = bool(event_rows) and any(any(row.values()) for row in event_rows)
    is_complete=bool(general) and not general_is_error and expected_items and items_have_units and events_have_data and len(event_rows)>0 and not errors
    meta={
      "status":"COMPLETO" if is_complete else ("PARCIAL" if raw else "FALHA"),
      "capturado_em_utc":captured,"url_contratacao":args.url,"cnpj":cnpj,"ano":year,"sequencial":seq,
      "endpoints_consultados":{"geral":general_endpoint,"itens":items_endpoint,"eventos":events_endpoint,"fallback_geral":PROPOSTA_URL},
      "fonte_dados_gerais":general_source,
      "base_api_consulta":CONSULTA_ROOT,
      "base_api_itens_historico":API_ROOT,
      "documentacao_api_consulta":"https://pncp.gov.br/api/consulta/swagger-ui/index.html",
      "documentacao_api_itens_historico":"https://pncp.gov.br/manual/pt-br/latest/contratacao/consultar_historico_da_contratacao.html",
      "erros_por_endpoint":errors,"avisos_por_endpoint":warnings,
      "quantidade_itens":len(item_rows),"quantidade_eventos":len(event_rows),
      "quantidade_itens_esperada":14,
      "observacao":"Os campos usam somente dados retornados pela API oficial. A consulta geral usa a rota de detalhe e, se ela retornar 404, procura o identificador PNCP exato nas listas oficiais. A modalidade Dispensa corresponde ao código 100 (código 8 é Pré-qualificação). A extração só é marcada COMPLETO quando dados gerais válidos, 14 itens com unidade e histórico com dados são recuperados."
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
