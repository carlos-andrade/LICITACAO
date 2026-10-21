# Proposta de atualização e validação da distribuição GOVERNANCA

| Campo | Valor |
|---|---|
| **ID** | LIC-GOV-DIST-001 |
| **Projeto** | LICITACAO |
| **Repositório** | [carlos-andrade/LICITACAO](https://github.com/carlos-andrade/LICITACAO) |
| **Tipo documental** | RELATORIO_DE_VALIDACAO |
| **Fase** | Adoção de governança — distribuição upstream |
| **Estado** | VALIDADA_COM_LIMITACOES |
| **Versão** | 0.2.0 |
| **Data de atualização** | 2026-10-21 |
| **Responsável** | Carlos Andrade, conforme registo-mestre |
| **Aprovador** | Carlos Andrade — decisão de adoção registada em 2026-10-21 |
| **Origem** | [GOVERNANCA/main](https://github.com/carlos-andrade/GOVERNANCA/tree/main) |
| **Autoridade superior** | [Constituição da GOVERNANCA](https://github.com/carlos-andrade/GOVERNANCA/blob/main/CONSTITUICAO.md) |

## Objetivo

Registar uma proposta de atualização do snapshot de normas GOVERNANCA no LICITACAO, mantendo a política `pull_request_only`, sem merge automático e sem alterar a habilitação do projeto no registo central.

## Evidência de comparação

A referência de origem foi atualizada para o commit `4da3029356e446ecbc6303124fc8019ee188450b`. A PR [#24](https://github.com/carlos-andrade/LICITACAO/pull/24) foi integrada. A comparação pós-merge confirmou 79/79 Git blob SHA coincidentes entre origem e destino, sem divergências.

A comparação pós-merge demonstra igualdade de conteúdo para todos os 79 ficheiros incluídos na PR. O check `validate` concluiu com sucesso e a checklist documental WATCHDOG foi executada; os sete controlos sem evidência permanecem UNKNOWN.

## Estado da PR de distribuição

- PR: [#24 — distribuição integral dos documentos normativos publicados](https://github.com/carlos-andrade/LICITACAO/pull/24), integrada.
- Check obrigatório `validate`: PASS na [execução pós-merge](https://github.com/carlos-andrade/LICITACAO/actions/runs/39623794138).
- Estado da distribuição: VALIDADA — 79/79 hashes coincidentes após o merge.

## Conteúdo da proposta

- Atualizar `source_commit` e as referências canónicas no manifesto.
- Estado do manifesto atualizado para `adoption_status: APROVADO_COM_LIMITACOES` na PR de alinhamento documental #25.
- Preservar a política `distribution_policy: pull_request_only`.
- Manter os bloqueios de adoção e validação operacional explícitos.
- Submeter a alteração a revisão por pull request; não executar merge automaticamente.

## Validação ainda necessária

1. Verificar o diff da PR e confirmar que os destinos locais não são sobrescritos indevidamente.
2. Executar a validação automatizada aplicável e registar o resultado real do workflow.
3. Demonstrar o processo de distribuição ponta a ponta por PR, incluindo geração da proposta, checks, revisão e ausência de merge automático.
4. Checklist WATCHDOG executada: 1 PASS e 7 UNKNOWN; os UNKNOWN permanecem limitações operacionais.
5. A adoção documental foi aprovada com limitações; integração do alinhamento final aguarda a PR #25.
6. A ativação central foi efetivada pela [GOVERNANCA PR #32](https://github.com/carlos-andrade/GOVERNANCA/pull/32) após integração da PR #25.

## Resultado

**Estado: VALIDADA_COM_LIMITACOES / G0 aprovado.** A distribuição integral dos 79 ficheiros de texto está comprovada por hashes e CI pós-merge. Os controlos WATCHDOG UNKNOWN continuam limitações operacionais; a ativação central foi efetivada pela [GOVERNANCA PR #32](https://github.com/carlos-andrade/GOVERNANCA/pull/32); `LICITACAO.enabled=true` indica âmbito de distribuição, não certificação operacional.
