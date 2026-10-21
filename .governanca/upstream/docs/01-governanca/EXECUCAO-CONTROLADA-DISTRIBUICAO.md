# Execução controlada da distribuição GOVERNANCA

| Campo | Valor |
|---|---|
| ID | GOV-DIST-PILOT-001 |
| Estado | PENDENTE DE EXECUÇÃO REAL |
| Data de preparação | 2026-10-21 |
| Repositório de origem | https://github.com/carlos-andrade/GOVERNANCA |
| Destino de piloto | carlos-andrade/STOCKS |
| Política | Pull Request apenas; sem merge automático |

## 1. Diagnóstico verificado

A execução [39521614567](https://github.com/carlos-andrade/GOVERNANCA/actions/runs/39521614567) validou o registo e a autenticação, mas o job de propagação falhou com:

`--allow-disabled-test exige --repo com um destino explícito`

A execução foi iniciada com `allow_disabled_test=true` e destino vazio. O comportamento é fail-closed: nenhuma distribuição real foi demonstrada por esse run. O erro não prova que o token esteja inválido nem que o destino tenha permissões de escrita.

## 2. Parâmetros para o piloto real

Executar o workflow **Propagar regras canónicas da GOVERNANCA** em `main` através de Actions → Run workflow com estes valores:

| Input | Valor |
|---|---|
| `dry_run` | `false` |
| `repository` | `carlos-andrade/STOCKS` |
| `allow_disabled_test` | `false` |

Não usar `allow_disabled_test=true` para o piloto STOCKS. Esse parâmetro destina-se exclusivamente ao repositório desativado LICITACAO e exige um destino explícito.

## 3. Evidências obrigatórias para aceitar o piloto

- [ ] O job `validar` termina em `success`.
- [ ] A autenticação identifica `carlos-andrade`; nenhum segredo aparece nos logs.
- [ ] O job `propagar` termina em `success` e o relatório JSON indica modo `pull-request`, zero erros e destino STOCKS.
- [ ] A Pull Request criada/atualizada é identificada por URL real.
- [ ] A branch e o diff contêm apenas `.governanca/upstream/` e o manifesto.
- [ ] O manifesto contém o commit de origem e hashes SHA-256.
- [ ] A PR não é integrada automaticamente; a revisão do consumidor permanece obrigatória.
- [ ] Uma segunda execução não cria PR duplicada nem alterações desnecessárias; registar o resultado `PR_UPDATED` ou `NO_CHANGE`.

Se a execução falhar em clone/push/create_pr, registar o erro sanitizado e corrigir permissões mínimas da credencial para o destino, sem expor ou copiar o token.

## 4. Estado de aceitação

**PENDENTE.** Este documento é um runbook, não prova execução. Só mudar para PASS depois de anexar o URL do run, URL da PR e artefacto de relatório observados no GitHub.
