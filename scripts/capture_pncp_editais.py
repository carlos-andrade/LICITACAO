#!/usr/bin/env python3
"""Coleta editais PNCP com propostas abertas via API oficial.

Exemplo:
  python scripts/capture_pncp_editais.py
  python scripts/capture_pncp_editais.py --data-final 20261031 --max-pages 10
"""
from __future__ import annotations
import argparse, csv, json, logging, re, time
from datetime import date, datetime, timezone
from pathlib import Path
from typing import Any
import requests

API = "https://pncp.gov.br/api/consulta/v1/contratacoes/proposta"
APP = "https://pncp.gov.br/app/editais"
COLS = ["numero_controle_pncp","numero_compra","ano_compra","modalidade_id","modalidade_nome","situacao","objeto","orgao_cnpj","orgao_nome","unidade_codigo","unidade_nome","uf","municipio","data_publicacao_pncp","data_atualizacao","data_abertura_proposta","data_encerramento_proposta","valor_total_estimado","valor_total_homologado","srp","amparo_legal","modo_disputa","fonte_sistema","link_sistema_origem","link_pncp","capturado_em_utc"]
UA = "LICITACAO-PNCP-Capture/1.0 (+https://github.com/carlos-andrade/LICITACAO)"

def val(x: Any) -> str:
    if x is None: return ""
    if isinstance(x, bool): return "Sim" if x else "Não"
    if isinstance(x, (dict,list)): return json.dumps(x,ensure_ascii=False,sort_keys=True)
    return re.sub(r"\s+"," ",str(x)).strip()

def pick(d: dict, *keys: str, default=""):
    for k in keys:
        x=d.get(k)
        if x not in (None,"",[],{}): return x
    return default

def obj(d: dict, key: str) -> dict:
    x=d.get(key,{})
    return x if isinstance(x,dict) else {}

def edital_url(d: dict) -> str:
    control=val(pick(d,"numeroControlePNCP","numeroControlePncp"))
    if control:
        # Número de controle: CNPJ-modalidade-sequencial/ano; monta rota conforme o PNCP.
        m=re.fullmatch(r"(\\d{14})-(\\d+)-(\\d+)/(\\d{4})",control)
        if m:
            cnpj, modalidade, seq, ano=m.groups()
            return f"https://pncp.gov.br/app/editais/{cnpj}/{ano}/{seq}"
        return APP + "?id=" + requests.utils.quote(control)
    return APP

def flatten(d: dict, captured: str) -> dict[str,str]:
    org, unit, legal = obj(d,"orgaoEntidade"), obj(d,"unidadeOrgao"), obj(d,"amparoLegal")
    return {
      "numero_controle_pncp":val(pick(d,"numeroControlePNCP","numeroControlePncp")),
      "numero_compra":val(pick(d,"numeroCompra","numeroProcesso","numero")),
      "ano_compra":val(pick(d,"anoCompra","ano")),
      "modalidade_id":val(pick(d,"modalidadeId","codigoModalidadeContratacao")),
      "modalidade_nome":val(pick(d,"modalidadeNome","nomeModalidade","modalidade")),
      "situacao":val(pick(d,"situacaoCompraNome","situacaoNome","situacaoCompraId","situacao")),
      "objeto":val(pick(d,"objetoCompra","objeto","informacaoComplementar")),
      "orgao_cnpj":val(pick(org,"cnpj",default=pick(d,"cnpjOrgao","cnpj"))),
      "orgao_nome":val(pick(org,"razaoSocial","nome",default=pick(d,"nomeOrgao"))),
      "unidade_codigo":val(pick(unit,"codigoUnidade","codigo",default=pick(d,"codigoUnidadeAdministrativa"))),
      "unidade_nome":val(pick(unit,"nomeUnidade","nome",default=pick(d,"unidadeNome"))),
      "uf":val(pick(unit,"uf",default=pick(d,"uf"))),
      "municipio":val(pick(unit,"municipioNome","nomeMunicipio",default=pick(d,"municipioNome","municipio"))),
      "data_publicacao_pncp":val(pick(d,"dataPublicacaoPncp","dataPublicacao","dataInclusao")),
      "data_atualizacao":val(pick(d,"dataAtualizacao","dataAtualizacaoGlobal")),
      "data_abertura_proposta":val(pick(d,"dataAberturaProposta","dataInicioRecebimentoPropostas")),
      "data_encerramento_proposta":val(pick(d,"dataEncerramentoProposta","dataFimRecebimentoPropostas")),
      "valor_total_estimado":val(pick(d,"valorTotalEstimado","valorTotalEstimadoCompra","valorTotal")),
      "valor_total_homologado":val(pick(d,"valorTotalHomologado")),
      "srp":val(pick(d,"srp","registroPreco")),
      "amparo_legal":val(pick(legal,"nome","descricao",default=pick(d,"amparoLegalNome"))),
      "modo_disputa":val(pick(d,"modoDisputaNome","modoDisputaId")),
      "fonte_sistema":val(pick(d,"nomeUsuario","usuarioNome","fonte")),
      "link_sistema_origem":val(pick(d,"linkSistemaOrigem","linkProcessoEletronico")),
      "link_pncp":edital_url(d),
      "capturado_em_utc":captured,
    }

def records_from(payload: dict):
    for k in ("data","items","content","resultado","contratacoes","lista"):
        if isinstance(payload.get(k),list): return payload[k]
    for v in payload.values():
        if isinstance(v,list) and (not v or isinstance(v[0],dict)): return v
    return []

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--data-final",default=date.today().strftime("%Y%m%d"))
    ap.add_argument("--modality",type=int,default=8)
    ap.add_argument("--page-size",type=int,default=50)
    ap.add_argument("--max-pages",type=int,default=0,help="0 = continuar até não haver mais registros")
    ap.add_argument("--max-records",type=int,default=0)
    ap.add_argument("--delay",type=float,default=1.0)
    ap.add_argument("--output-dir",default="EDITAIS")
    args=ap.parse_args()
    if not re.fullmatch(r"\d{8}",args.data_final): ap.error("--data-final deve ser AAAAMMDD")
    if not 10<=args.page_size<=50: ap.error("--page-size deve estar entre 10 e 50")
    if args.delay<0: ap.error("--delay não pode ser negativo")
    logging.basicConfig(level=logging.INFO,format="%(asctime)s %(levelname)s %(message)s")
    out=Path(args.output_dir); out.mkdir(parents=True,exist_ok=True)
    s=requests.Session(); s.headers.update({"Accept":"application/json","User-Agent":UA})
    captured=datetime.now(timezone.utc).isoformat(timespec="seconds")
    rows=[]; raw=[]; seen=set(); page=1; total_pages=None; total_records=None
    params_base={"dataFinal":args.data_final,"codigoModalidadeContratacao":args.modality,"tamanhoPagina":args.page_size}
    try:
      while not args.max_pages or page<=args.max_pages:
        params={**params_base,"pagina":page}
        for attempt in range(5):
          try:
            resp=s.get(API,params=params,timeout=60)
            if resp.status_code in (429,500,502,503,504): raise requests.HTTPError(f"HTTP {resp.status_code}")
            resp.raise_for_status(); payload=resp.json(); break
          except (requests.RequestException,ValueError) as e:
            if attempt==4: raise RuntimeError(f"Falha na página {page}: {e}")
            time.sleep(min(2**attempt,30))
        if total_pages is None:
          for k in ("totalPaginas","totalPaginasEncontradas","pages"):
            try: total_pages=int(payload[k]); break
            except (KeyError,TypeError,ValueError): pass
        if total_records is None:
          for k in ("totalRegistros","total","totalElements"):
            try: total_records=int(payload[k]); break
            except (KeyError,TypeError,ValueError): pass
        batch=records_from(payload)
        if not batch:
          logging.info("Página %d sem registros; encerrando.",page); break
        added=0
        for item in batch:
          row=flatten(item,captured)
          key=row["numero_controle_pncp"] or "|".join((row["orgao_cnpj"],row["ano_compra"],row["numero_compra"],row["objeto"]))
          if key in seen: continue
          seen.add(key); rows.append(row); raw.append(item); added+=1
          if args.max_records and len(rows)>=args.max_records: break
        logging.info("Página %d: %d devolvidos, %d novos, %d acumulados.",page,len(batch),added,len(rows))
        if args.max_records and len(rows)>=args.max_records: break
        if total_pages is not None and page>=total_pages: break
        if len(batch)<args.page_size: break
        page+=1; time.sleep(args.delay)
    except Exception as e:
      meta={"status":"PARCIAL_COM_ERRO","erro":str(e),"capturado_em_utc":captured,"paginas_consultadas":page,"registros_unicos_capturados":len(rows),"dataFinal":args.data_final,"codigoModalidadeContratacao":args.modality}
      (out/"pncp-editais-metadados.json").write_text(json.dumps(meta,ensure_ascii=False,indent=2),encoding="utf-8")
      logging.error("%s",e); return 2
    complete=(total_pages is None or page>=total_pages or (total_records is not None and len(rows)>=total_records))
    meta={
      "status":"COMPLETO" if complete and not args.max_pages else "CAPTURA_COM_LIMITE_CONFIGURADO",
      "capturado_em_utc":captured,"url_origem":APP+"?pagina=1&status=recebendo_proposta&tam_pagina=100&tem_nfe_contrato=false&indicador_orcamento_sigiloso=false&modalidades="+str(args.modality),
      "api_endpoint":API,"dataFinal":args.data_final,"codigoModalidadeContratacao":args.modality,"tamanhoPaginaAPI":args.page_size,
      "filtros_da_tela_registrados_na_origem":{"status":"recebendo_proposta","tam_pagina":100,"tem_nfe_contrato":False,"indicador_orcamento_sigiloso":False,"modalidades":[args.modality]},
      "nota_filtros":"O endpoint /contratacoes/proposta oferece recebimento aberto e filtro de modalidade. Os parâmetros tem_nfe_contrato e indicador_orcamento_sigiloso não estão documentados para este endpoint, portanto não foram simulados.",
      "paginas_consultadas":page,"total_paginas_informado_pela_api":total_pages,"total_registros_informado_pela_api":total_records,"registros_unicos_capturados":len(rows),
      "limite_max_paginas_configurado":args.max_pages
    }
    with (out/"pncp-editais-abertos.csv").open("w",encoding="utf-8-sig",newline="") as f:
      w=csv.DictWriter(f,fieldnames=COLS,delimiter=";"); w.writeheader(); w.writerows(rows)
    (out/"pncp-editais-abertos.json").write_text(json.dumps(raw,ensure_ascii=False,indent=2),encoding="utf-8")
    (out/"pncp-editais-metadados.json").write_text(json.dumps(meta,ensure_ascii=False,indent=2),encoding="utf-8")
    try:
      from openpyxl import Workbook
      from openpyxl.styles import Alignment,Font,PatternFill
      from openpyxl.utils import get_column_letter
      wb=Workbook(); ws=wb.active; ws.title="Editais PNCP"; ws.append(COLS)
      for c in ws[1]:
        c.font=Font(bold=True,color="FFFFFF"); c.fill=PatternFill("solid",fgColor="17365D"); c.alignment=Alignment(wrap_text=True,vertical="top")
      for row in rows: ws.append([row.get(k,"") for k in COLS])
      ws.freeze_panes="A2"; ws.auto_filter.ref=ws.dimensions; ws.sheet_view.showGridLines=False; ws.row_dimensions[1].height=36
      for i,name in enumerate(COLS,1):
        n=max([len(name)]+[min(len(str(ws.cell(r,i).value or "")),60) for r in range(2,min(ws.max_row,250)+1)])
        ws.column_dimensions[get_column_letter(i)].width=min(max(n+2,12),50)
      m=wb.create_sheet("Metadados"); m.append(["Campo","Valor"])
      for k,v in meta.items(): m.append([k,json.dumps(v,ensure_ascii=False) if isinstance(v,(dict,list)) else str(v)])
      wb.save(out/"pncp-editais-abertos.xlsx")
    except ImportError: logging.warning("openpyxl indisponível; CSV/JSON foram gravados.")
    summary=f"""# Captura de Editais do PNCP

- **Status:** {meta['status']}
- **Capturado em UTC:** {captured}
- **Registros únicos:** {len(rows)}
- **Páginas consultadas:** {page}
- **Data final:** {args.data_final}
- **Modalidade (código):** {args.modality}
- **Fonte oficial:** [API de consulta do PNCP](https://pncp.gov.br/api/consulta/swagger-ui/index.html)
- **Tela de origem:** [PNCP — editais abertos]({meta['url_origem']})

## Arquivos

- [Tabela Excel](pncp-editais-abertos.xlsx)
- [Tabela CSV](pncp-editais-abertos.csv)
- [Dados brutos JSON](pncp-editais-abertos.json)
- [Metadados da coleta](pncp-editais-metadados.json)

## Limitações

A API usa `tamanhoPagina` com intervalo documentado de 10 a 50, portanto a extração é paginada em chamadas de até 50 registros. Os parâmetros `tem_nfe_contrato` e `indicador_orcamento_sigiloso` estão preservados no URL de origem, mas não são documentados para o endpoint de propostas abertas e não foram aplicados pela API.
"""
    (out/"README-CAPTURA-PNCP.md").write_text(summary,encoding="utf-8")
    logging.info("Concluído: %s; %s registros únicos.",meta["status"],len(rows))
    return 0
if __name__=="__main__": raise SystemExit(main())
