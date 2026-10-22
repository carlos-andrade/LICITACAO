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
| **SHA-256 (conteúdo canónico)** | c0beb15ea2605da0c6ba6c136eaec6c3412a046ffcbc52600f8153c1d2057349 |
| **Commit de referência (versão anterior)** | [43b405550ea6e3de2dcf6402df5e7292dcf3b25e](https://github.com/carlos-andrade/LICITACAO/commit/43b405550ea6e3de2dcf6402df5e7292dcf3b25e) |
| **Data de criação** | N/A — data histórica não verificada |
| **Data de atualização** | 2026-10-22 |
| **Responsável** | Responsável pelo projeto LICITAÇÃO |
| **Aprovador** | Pendente — não há evidência de aprovação neste documento |
| **Origem** | Conteúdo existente no repositório; caminho: `EDITAIS/README-CAPTURA-PNCP.md` |
| **Autoridade superior** | [Constituição do projeto](https://github.com/carlos-andrade/LICITACAO/blob/main/CONSTITUICAO.md) |
| **Cadeia de autoridade** | PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO |

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
