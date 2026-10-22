# Capturador integral PNCP

| Campo | Valor |
|---|---|
| **ID** | LIC-DOC-SCRIPTS-README-CAPTURA-INTEGRAL-MD-E29DEC8C |
| **Projeto** | LICITAÇÃO |
| **Repositório** | [carlos-andrade/LICITACAO](https://github.com/carlos-andrade/LICITACAO) |
| **Tipo documental** | DOCUMENTO_TECNICO |
| **Fase** | N/A — fase não definida no conteúdo de origem |
| **Estado** | EM_REVISAO |
| **Versão** | 1.0.0 |
| **SHA-256 (conteúdo canónico)** | b0661550851abece8fb5f90aa9d557b6873d396c02a47c45264b78983c144b54 |
| **Commit de referência (versão anterior)** | [b5e445630ceaf57fac58ae963dbedc587d836e52](https://github.com/carlos-andrade/LICITACAO/commit/b5e445630ceaf57fac58ae963dbedc587d836e52) |
| **Data de criação** | N/A — data histórica não verificada |
| **Data de atualização** | 2026-10-22 |
| **Responsável** | Responsável pelo projeto LICITAÇÃO |
| **Aprovador** | Pendente — não há evidência de aprovação neste documento |
| **Origem** | Conteúdo existente no repositório; caminho: `scripts/README-captura-integral.md` |
| **Autoridade superior** | [Constituição do projeto](https://github.com/carlos-andrade/LICITACAO/blob/main/CONSTITUICAO.md) |
| **Cadeia de autoridade** | PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO |

Este script tenta reunir em uma execução:
- detalhes e endpoints comuns da contratação;
- itens;
- arquivos/documentos;
- atas de registro de preço;
- contratos e empenhos;
- histórico;
- HTML e texto renderizados;
- links e respostas JSON observados no tráfego de rede do navegador.

## Instalação

```bash
python -m pip install requests beautifulsoup4 playwright
python -m playwright install chromium
```

## Execução para o processo de exemplo

```bash
python scripts/pncp_capture_integral.py "https://pncp.gov.br/app/editais/33663683000116/2026/548" --output-dir EDITAIS --download-files
```

Gera:
- `AAAA-SEQ-CNPJ-captura-integral.json`: respostas de API, HTML/texto, frames, links, respostas de rede e diagnósticos;
- `AAAA-SEQ-CNPJ-todos-campos.csv`: cada campo encontrado nas respostas JSON, com endpoint e caminho do campo;
- `AAAA-SEQ-CNPJ-captura-integral.md`: resumo de diagnóstico e cobertura das cinco seções;
- opcionalmente, diretório `*_arquivos/` com os links identificados que puderem ser baixados.

## O que significa “tudo”

O script combina endpoints comuns da API e uma sessão real de Chromium via Playwright. A interface do PNCP pode mudar e os endpoints de atas/contratos/empenhos/histórico podem depender de outras rotas ou paginação. Por isso o JSON bruto e os diagnósticos são parte essencial da captura: resposta HTTP com erro não significa que a seção esteja vazia. Confira os parâmetros de paginação e os totais retornados antes de considerar uma lista completa.

O download de um PDF ou arquivo Office não extrai seu conteúdo interno. Para obter tabelas e texto desses anexos, rode uma etapa de parsing/OCR separada. Não trate a ausência de campos como prova de ausência da informação.

Fontes oficiais: [API de Consulta PNCP](https://pncp.gov.br/api/consulta/swagger-ui/index.html) · [Manual PNCP](https://pncp.gov.br/manual/pt-br/latest/).
