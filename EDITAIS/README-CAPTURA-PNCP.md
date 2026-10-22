# Captura de Editais do PNCP

| Campo | Valor |
|---|---|
| **ID** | LIC-DOC-EDITAIS-README-CAPTURA-PNCP-MD-B9D9F42A |
| **Projeto** | LICITAÇÃO |
| **Repositório** | [carlos-andrade/LICITACAO](https://github.com/carlos-andrade/LICITACAO) |
| **Tipo documental** | DOCUMENTO_TECNICO |
| **Fase** | N/A — fase não definida no conteúdo de origem |
| **Estado** | EM_REVISAO |
| **Versão** | 1.0.0 |
| **SHA-256 (conteúdo canónico)** | 355100f585eefa61c269a9f635c8c735d4a81292165a8c4f59dee4f868702ab2 |
| **Commit de referência (versão anterior)** | [8f69f4c4ecacc44c8fbdc88712f23611bb711e67](https://github.com/carlos-andrade/LICITACAO/commit/8f69f4c4ecacc44c8fbdc88712f23611bb711e67) |
| **Data de criação** | N/A — data histórica não verificada |
| **Data de atualização** | 2026-10-22 |
| **Responsável** | Responsável pelo projeto LICITAÇÃO |
| **Aprovador** | Pendente — não há evidência de aprovação neste documento |
| **Origem** | Conteúdo existente no repositório; caminho: `EDITAIS/README-CAPTURA-PNCP.md` |
| **Autoridade superior** | [Constituição do projeto](https://github.com/carlos-andrade/LICITACAO/blob/main/CONSTITUICAO.md) |
| **Cadeia de autoridade** | PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO |

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
