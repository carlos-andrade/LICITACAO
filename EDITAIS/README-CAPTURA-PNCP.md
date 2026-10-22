# Coleta automatizada de editais do PNCP

## Fonte e objetivo
Tela solicitada: https://pncp.gov.br/app/editais?pagina=1&status=recebendo_proposta&tam_pagina=100&tem_nfe_contrato=false&indicador_orcamento_sigiloso=false&modalidades=8

O coletor usa a API oficial pública do PNCP, endpoint `GET /v1/contratacoes/proposta`, para obter contratações com recebimento de propostas aberto e modalidade código 8. Documentação: https://pncp.gov.br/api/consulta/swagger-ui/index.html

## Arquivos gerados
- `pncp-editais-abertos.xlsx`: tabela Excel filtrável com aba de metadados.
- `pncp-editais-abertos.csv`: tabela separada por ponto e vírgula.
- `pncp-editais-abertos.json`: dados brutos da API.
- `pncp-editais-metadados.json`: parâmetros, status e totalizadores.
- `README-CAPTURA-PNCP.md`: resumo da captura.

## Paginação e filtros
O coletor percorre as páginas da API, remove duplicidades pelo número de controle PNCP e respeita uma pausa configurável. A API normalmente aceita `tamanhoPagina` de 10 a 50; por isso, o parâmetro visual `tam_pagina=100` não é reproduzido literalmente na consulta API.
Os filtros `tem_nfe_contrato=false` e `indicador_orcamento_sigiloso=false` fazem parte da URL da interface, mas não estão documentados como parâmetros do endpoint de propostas abertas. O script não afirma que foram aplicados.

## Executar
GitHub → Actions → **Captura de editais PNCP** → **Run workflow**. Para captura completa, use `max_pages=0`. O workflow também está programado para dias úteis e envia os resultados atualizados ao diretório EDITAIS.
