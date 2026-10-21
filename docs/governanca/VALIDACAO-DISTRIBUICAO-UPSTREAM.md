# Evidência de validação da distribuição GOVERNANCA → LICITACAO

- **ID:** LIC-GOV-DIST-001
- **Estado:** PENDENTE — teste operacional ainda não executado
- **Repositório de origem:** [carlos-andrade/GOVERNANCA](https://github.com/carlos-andrade/GOVERNANCA)
- **Repositório de destino:** [carlos-andrade/LICITACAO](https://github.com/carlos-andrade/LICITACAO)
- **PR que prepara o modo de teste controlado:** [GOVERNANCA #21](https://github.com/carlos-andrade/GOVERNANCA/pull/21)
- **PR que formaliza a adoção proposta:** [LICITACAO #4](https://github.com/carlos-andrade/LICITACAO/pull/4)

## Estado factual

A infraestrutura de distribuição existente usa a política `pull_request_only`. O script cria/atualiza uma branch e abre/atualiza uma Pull Request; não executa merge.

O mecanismo atual filtra os destinos para incluir apenas `enabled: true`. Por isso, o teste de LICITACAO exige primeiro que a PR GOVERNANCA #21 seja revista, aprovada e integrada, incluindo a exceção de teste limitada a este repositório. Até lá, **não há evidência de que a distribuição para LICITACAO tenha sido executada com sucesso**.

## Procedimento de teste após a integração da GOVERNANCA #21

1. Confirmar que a PR #21 foi integrada por revisão humana autorizada e que os testes CI passaram.
2. No repositório GOVERNANCA, abrir Actions → **Propagar regras canónicas da GOVERNANCA** → Run workflow.
3. Primeira execução (simulação):
   - `dry_run=true`
   - `repository=carlos-andrade/LICITACAO`
   - `allow_disabled_test=true`
4. Confirmar no relatório que o destino único é LICITACAO e que o resultado é `WOULD_OPEN_PR`; guardar URL da execução e artefacto.
5. Segunda execução (publicação controlada):
   - `dry_run=false`
   - `repository=carlos-andrade/LICITACAO`
   - `allow_disabled_test=true`
6. Confirmar que o workflow termina sem erro, registar o artefacto `relatorio-propagacao-governanca` e identificar a PR criada/atualizada em LICITACAO.
7. Verificar o diff da PR de destino: ficheiros somente sob `.governanca/upstream/`, manifesto com commit de origem e hashes, sem sobrescrita de documentos locais.
8. Verificar que a PR permanece aberta e não foi integrada automaticamente; guardar URL, estado e data/hora da verificação.
9. Confirmar que o registo central continua com `enabled: false` durante o teste.

## Registo dos resultados

| Evidência | Resultado |
|---|---|
| Review e merge humano da GOVERNANCA #21 | PENDENTE |
| CI da GOVERNANCA #21 | EM EXECUÇÃO no momento da preparação deste documento |
| URL da execução dry-run | PENDENTE |
| Relatório dry-run / artefacto | PENDENTE |
| URL da execução de publicação controlada | PENDENTE |
| PR criada/atualizada em LICITACAO | PENDENTE |
| Diff confinado a `.governanca/upstream/` | PENDENTE |
| Confirmação de ausência de merge automático | PENDENTE |
| Verificação de `enabled: false` mantido durante o teste | PENDENTE |

## Critério de conclusão

Esta evidência só pode ser marcada como **APROVADA** quando as ligações e resultados reais forem registados e revistos. Não preencher resultados por inferência. Uma simulação bem-sucedida não substitui a execução real de publicação por PR.

A conclusão desta validação não aprova automaticamente a adoção da GOVERNANCA, não altera o registo central e não desbloqueia o Gate G0 de LICITACAO.
