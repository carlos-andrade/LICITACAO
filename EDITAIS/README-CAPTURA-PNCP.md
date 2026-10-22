# Coleta automatizada de editais do PNCP

| Campo | Valor |
|---|---|
| **ID** | LIC-DOC-EDITAIS-README-CAPTURA-PNCP-MD-B9D9F42A |
| **Projeto** | LICITAÇÃO |
| **Repositório** | [carlos-andrade/LICITACAO](https://github.com/carlos-andrade/LICITACAO) |
| **Tipo documental** | DOCUMENTO_TECNICO |
| **Fase** | N/A — fase não definida no conteúdo de origem |
| **Estado** | EM_REVISAO |
| **Versão** | 1.0.0 |
| **SHA-256 (conteúdo canónico)** | 983062314eb1c5e6c6b18d3a0f0202fe8f6f449b1c6c1db72453a33fa24b1873 |
| **Commit de referência (versão anterior)** | [8aa16bfcf449724d38f9568be4b1aeb637df7771](https://github.com/carlos-andrade/LICITACAO/commit/8aa16bfcf449724d38f9568be4b1aeb637df7771) |
| **Data de criação** | N/A — data histórica não verificada |
| **Data de atualização** | 2026-10-22 |
| **Responsável** | Responsável pelo projeto LICITAÇÃO |
| **Aprovador** | Pendente — não há evidência de aprovação neste documento |
| **Origem** | Conteúdo existente no repositório; caminho: `EDITAIS/README-CAPTURA-PNCP.md` |
| **Autoridade superior** | [Constituição do projeto](https://github.com/carlos-andrade/LICITACAO/blob/main/CONSTITUICAO.md) |
| **Cadeia de autoridade** | PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO |

## Fonte e objetivo
Tela solicitada: https://pncp.gov.br/app/editais?pagina=1&status=recebendo_proposta&tam_pagina=100&tem_nfe_contrato=false&indicador_orcamento_sigiloso=false&modalidades=8

O coletor usa a API oficial pública do PNCP, endpoint `GET /v1/contratacoes/proposta`, para obter contratações com recebimento de propostas aberto e modalidade código 8. A documentação oficial está em https://pncp.gov.br/api/consulta/swagger-ui/index.html.

## Arquivos gerados
- `pncp-editais-abertos.xlsx`: tabela Excel filtrável com aba de metadados.
- `pncp-editais-abertos.csv`: tabela separada por ponto e vírgula, UTF-8 com BOM.
- `pncp-editais-abertos.json`: dados brutos retornados pela API.
- `pncp-editais-metadados.json`: parâmetros, status, data/hora e totalizadores.
- `README-CAPTURA-PNCP.md`: resumo da captura.

## Paginação e filtros
A documentação da API informa que o endpoint de propostas abertas usa `dataFinal`, `pagina`, código de modalidade, e tamanho de página. O coletor caminha por todas as páginas detectadas (ou até resposta vazia), remove duplicidades pelo número de controle PNCP e respeita pausa entre requisições. A API tipicamente aceita `tamanhoPagina` entre 10 e 50, portanto o valor da tela `tam_pagina=100` não pode ser replicado literalmente no endpoint.
Os parâmetros `tem_nfe_contrato=false` e `indicador_orcamento_sigiloso=false` ficam documentados como parte da tela solicitada, mas não constam como filtros do endpoint da API consultado. O script não afirma que esses filtros foram aplicados.

## Como executar
GitHub → Actions → **Captura de editais PNCP** → **Run workflow**. Para a captura completa, use `max_pages=0`. O workflow também foi configurado para execução em dias úteis e publica resultados atualizados na pasta EDITAIS.
