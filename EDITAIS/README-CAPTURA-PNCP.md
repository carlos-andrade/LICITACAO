# Captura de Editais do PNCP

- **Status:** COMPLETO
- **Capturado em UTC:** 2026-10-22T20:39:20+00:00
- **Registros únicos:** 45
- **Páginas consultadas:** 1
- **Data final:** 20261022
- **Modalidade (código):** 8
- **Fonte oficial:** [API de consulta do PNCP](https://pncp.gov.br/api/consulta/swagger-ui/index.html)
- **Tela de origem:** [PNCP — editais abertos](https://pncp.gov.br/app/editais?pagina=1&status=recebendo_proposta&tam_pagina=100&tem_nfe_contrato=false&indicador_orcamento_sigiloso=false&modalidades=8)

## Arquivos

- [Tabela Excel](pncp-editais-abertos.xlsx)
- [Tabela CSV](pncp-editais-abertos.csv)
- [Dados brutos JSON](pncp-editais-abertos.json)
- [Metadados da coleta](pncp-editais-metadados.json)

## Limitações

A API usa `tamanhoPagina` com intervalo documentado de 10 a 50, portanto a extração é paginada em chamadas de até 50 registros. Os parâmetros `tem_nfe_contrato` e `indicador_orcamento_sigiloso` estão preservados no URL de origem, mas não são documentados para o endpoint de propostas abertas e não foram aplicados pela API.
