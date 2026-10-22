# Coleta automatizada de editais do PNCP

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
