# Proposta de atualização e validação da distribuição GOVERNANCA

| Campo | Valor |
|---|---|
| **ID** | LIC-GOV-DIST-001 |
| **Projeto** | LICITACAO |
| **Repositório** | [carlos-andrade/LICITACAO](https://github.com/carlos-andrade/LICITACAO) |
| **Tipo documental** | RELATORIO_DE_VALIDACAO |
| **Fase** | Adoção de governança — distribuição upstream |
| **Estado** | EM_REVISAO |
| **Versão** | 0.2.0 |
| **Data de atualização** | 2026-10-21 |
| **Responsável** | Pendente de confirmação formal |
| **Aprovador** | Pendente |
| **Origem** | [GOVERNANCA/main](https://github.com/carlos-andrade/GOVERNANCA/tree/main) |
| **Autoridade superior** | [Constituição da GOVERNANCA](https://github.com/carlos-andrade/GOVERNANCA/blob/main/CONSTITUICAO.md) |

## Objetivo

Registar uma proposta de atualização do snapshot de normas GOVERNANCA no LICITACAO, mantendo a política `pull_request_only`, sem merge automático e sem alterar a habilitação do projeto no registo central.

## Evidência de comparação

A referência de origem foi atualizada para o commit `4da3029356e446ecbc6303124fc8019ee188450b`. A PR [#23](https://github.com/carlos-andrade/LICITACAO/pull/23) distribui 79 ficheiros de texto abrangidos pelos `published_roots` do registo-mestre. A comparação pré-PR da árvore Git confirmou 79/79 Git blob SHA coincidentes entre origem e destino proposto, sem divergências.

A comparação demonstra igualdade de conteúdo para todos os 79 ficheiros incluídos na PR. A validação operacional final exige check `validate` concluído com sucesso, merge da PR, comparação pós-merge e execução documentada da checklist WATCHDOG.

## Estado da PR de distribuição

- PR: [#23 — distribuição integral dos documentos normativos publicados](https://github.com/carlos-andrade/LICITACAO/pull/23).
- Check obrigatório `validate`: em fila na última verificação; ainda sem conclusão.
- Estado da distribuição: submetida a revisão; não considerar concluída até merge e validação pós-merge.

## Conteúdo da proposta

- Atualizar `source_commit` e as referências canónicas no manifesto.
- Preservar o estado `adoption_status: EM_REVISAO`.
- Preservar a política `distribution_policy: pull_request_only`.
- Manter os bloqueios de adoção e validação operacional explícitos.
- Submeter a alteração a revisão por pull request; não executar merge automaticamente.

## Validação ainda necessária

1. Verificar o diff da PR e confirmar que os destinos locais não são sobrescritos indevidamente.
2. Executar a validação automatizada aplicável e registar o resultado real do workflow.
3. Demonstrar o processo de distribuição ponta a ponta por PR, incluindo geração da proposta, checks, revisão e ausência de merge automático.
4. Executar a checklist WATCHDOG local e documentar cada resultado com evidência.
5. Obter revisão independente e aprovação formal da adoção.
6. Só após aprovação individual e validação operacional, propor por PR a alteração de `LICITACAO.enabled` no registo central GOVERNANCA.

## Resultado

**Estado: EM_REVISAO / G0 continua bloqueado.** Esta PR atualiza a referência documental do snapshot e regista o âmbito da comparação. Não é prova de que a distribuição completa foi executada nem autoriza ativar LICITACAO.
