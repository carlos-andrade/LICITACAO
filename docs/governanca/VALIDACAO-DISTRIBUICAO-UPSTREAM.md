# Evidência de validação da distribuição GOVERNANCA → LICITACAO

| Campo | Valor |
|---|---|
| **ID** | LIC-DOC-CS-GOVERNANCA-VALIDACAO-DISTRIBUICAO-UPSTREAM-MD-E8D6FAC4 |
| **Projeto** | LICITAÇÃO |
| **Repositório** | [carlos-andrade/LICITACAO](https://github.com/carlos-andrade/LICITACAO) |
| **Tipo documental** | DOCUMENTO_TECNICO |
| **Fase** | N/A — fase não definida no conteúdo de origem |
| **Estado** | EM_REVISAO |
| **Versão** | 1.0.0 |
| **SHA-256 (conteúdo canónico)** | 3dedc89c10665899d3b2f0a8d52976972dbc1dc2a46c0f1124aa24dbe23a1c44 |
| **Commit de referência (versão anterior)** | [b5e445630ceaf57fac58ae963dbedc587d836e52](https://github.com/carlos-andrade/LICITACAO/commit/b5e445630ceaf57fac58ae963dbedc587d836e52) |
| **Data de criação** | N/A — data histórica não verificada |
| **Data de atualização** | 2026-10-22 |
| **Responsável** | Responsável pelo projeto LICITAÇÃO |
| **Aprovador** | Pendente — não há evidência de aprovação neste documento |
| **Origem** | Conteúdo existente no repositório; caminho: `docs/governanca/VALIDACAO-DISTRIBUICAO-UPSTREAM.md` |
| **Autoridade superior** | [Constituição do projeto](https://github.com/carlos-andrade/LICITACAO/blob/main/CONSTITUICAO.md) |
| **Cadeia de autoridade** | PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO |

- **ID:** LIC-GOV-DIST-001
- **Estado:** BLOQUEADO — execução operacional real pendente
- **Última verificação:** 2026-10-21
- **Repositório de origem:** [carlos-andrade/GOVERNANCA](https://github.com/carlos-andrade/GOVERNANCA)
- **Repositório de destino:** [carlos-andrade/LICITACAO](https://github.com/carlos-andrade/LICITACAO)
- **PR do modo de teste controlado:** [GOVERNANCA #21](https://github.com/carlos-andrade/GOVERNANCA/pull/21)
- **PR da proposta de adoção:** [LICITACAO #4](https://github.com/carlos-andrade/LICITACAO/pull/4)
- **Acompanhamento:** [LICITACAO #6 — concluir Gate G0 e validar distribuição upstream](https://github.com/carlos-andrade/LICITACAO/issues/6)

## Estado verificado

A PR GOVERNANCA #21 está integrada. A PR LICITACAO #4 também está integrada. A consulta à API de reviews de ambas devolveu listas vazias: não existe review de aprovação registada nas evidências consultadas. Por isso, a integração não deve ser descrita como aprovação humana comprovada.

A execução [39520440947](https://github.com/carlos-andrade/GOVERNANCA/actions/runs/39520440947) terminou com sucesso, mas o nome do workflow é **Governance Integration — validação F1/F2**. É evidência de CI da PR #21, não é uma execução do workflow de distribuição para LICITACAO e não comprova a criação de uma PR de sincronização.

O workflow oficial [Propagar regras canónicas da GOVERNANCA](https://github.com/carlos-andrade/GOVERNANCA/blob/main/.github/workflows/propagar-regras-governanca.yml) disponibiliza `workflow_dispatch` com os parâmetros de teste controlado. A integração disponível nesta sessão não expõe uma ação para disparar `workflow_dispatch`; portanto, não se afirma que o teste foi executado.

A leitura atual do registo central mantém `carlos-andrade/LICITACAO` com `enabled: false`. A consulta atual não encontrou PRs abertas em LICITACAO nem em GOVERNANCA. A issue #6 consolida as ações pendentes, mas não constitui evidência de que tenham sido executadas.

## Procedimento para concluir o teste

1. Abrir o workflow [Propagar regras canónicas da GOVERNANCA](https://github.com/carlos-andrade/GOVERNANCA/actions/workflows/propagar-regras-governanca.yml) no GitHub e escolher **Run workflow**.
2. Executar primeiro a simulação com:
   - `dry_run=true`
   - `repository=carlos-andrade/LICITACAO`
   - `allow_disabled_test=true`
3. Guardar a URL da execução e o artefacto `relatorio-propagacao-governanca`; confirmar que o relatório identifica apenas LICITACAO e o resultado `WOULD_OPEN_PR`.
4. Só depois da simulação validada, executar publicação controlada com:
   - `dry_run=false`
   - `repository=carlos-andrade/LICITACAO`
   - `allow_disabled_test=true`
5. Guardar URL da execução, relatório e URL da PR criada/atualizada em LICITACAO.
6. Verificar o diff: alterações confinadas a `.governanca/upstream/`, manifesto com commit de origem e hashes, sem sobrescrita de documentos locais.
7. Confirmar que a PR de sincronização permanece aberta e não foi integrada automaticamente.
8. Confirmar que o registo central continua com `enabled: false` durante o teste.

## Matriz de evidências

| Evidência | Resultado verificado |
|---|---|
| PR GOVERNANCA #21 integrada | SIM |
| Review APPROVE registada na PR #21 | NÃO ENCONTRADA |
| CI da PR #21 | SUCESSO; execução 39520440947, workflow de validação F1/F2 |
| PR LICITACAO #4 integrada | SIM |
| Review APPROVE registada na PR #4 | NÃO ENCONTRADA |
| Execução dry-run do workflow de distribuição | PENDENTE |
| Relatório/artefacto da simulação | PENDENTE |
| Execução real de publicação controlada | PENDENTE |
| PR de sincronização criada pelo workflow | PENDENTE |
| Diff da PR verificado | PENDENTE |
| Ausência de merge automático verificada | PENDENTE |
| `enabled: false` mantido | CONFIRMADO na última leitura do registo central |

## Critério de conclusão

Esta validação só pode ser marcada como **APROVADA** quando as URLs, os relatórios e a PR real de destino forem registados e revistos. Não inferir a execução operacional a partir de testes unitários ou CI de outro workflow.

A adoção normativa, o teste de distribuição e o Gate G0 são controlos separados. Este documento não ativa o registo central, não certifica aprovação humana e não desbloqueia o Gate G0 de LICITACAO.
