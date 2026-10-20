# Inspeção de adoção da GOVERNANCA — LICITACAO

| Campo | Valor |
|---|---|
| **ID** | LIC-GOV-INSPEC-001 |
| **Projeto** | LICITACAO |
| **Repositório** | [carlos-andrade/LICITACAO](https://github.com/carlos-andrade/LICITACAO) |
| **Tipo documental** | RELATORIO_DE_INSPECAO |
| **Fase** | Adoção de governança |
| **Estado** | EM_REVISAO |
| **Versão** | 0.1.0 |
| **SHA-256 (conteúdo canónico)** | PENDENTE — calcular após validação final do conteúdo |
| **Commit de referência (versão anterior)** | [f42637de27d382049109e30bb7f05008815d45ef](https://github.com/carlos-andrade/LICITACAO/commit/f42637de27d382049109e30bb7f05008815d45ef) |
| **Data de criação** | 2026-10-20 |
| **Data de atualização** | 2026-10-20 |
| **Responsável** | Responsável do repositório — nomeação formal pendente |
| **Aprovador** | Pendente |
| **Origem** | Inspeção documental inicial das referências públicas da GOVERNANCA e do LICITACAO |
| **Autoridade superior** | [GOVERNANCA/CONSTITUICAO.md](https://github.com/carlos-andrade/GOVERNANCA/blob/main/CONSTITUICAO.md) |
| **Cadeia de autoridade** | PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO |

## Resultado

Esta inspeção prepara a adoção no LICITACAO; não é certificação de conformidade. A GOVERNANCA exige inspeção individual e declara que referência normativa ou espelhamento, por si só, não prova adoção.

## Fontes canónicas consultadas

- [Constituição](https://github.com/carlos-andrade/GOVERNANCA/blob/main/CONSTITUICAO.md) — princípios, hierarquia, gates e WATCHDOG.
- [Carta/Contrato de roadmap](https://github.com/carlos-andrade/GOVERNANCA/blob/main/CARTA-CONTRATO-PADRAO-ROADMAP.md) — adoção individual, fail-closed e evidências.
- [Roadmap padrão](https://github.com/carlos-andrade/GOVERNANCA/blob/main/ROADMAP-PADRAO-GOVERNANCA.md) — formato do plano executivo.
- [Norma de status](https://github.com/carlos-andrade/GOVERNANCA/blob/main/standards/status-e-percentual-de-conclusao.md) — scorecard 20/60/20 e exigência de evidências.
- [Norma de cabeçalho](https://github.com/carlos-andrade/GOVERNANCA/blob/main/CABE%C3%87ALHO/NORMA-CABECALHO-PADRAO.md) — metadados documentais.
- [WATCHDOG](https://github.com/carlos-andrade/GOVERNANCA/blob/main/WATCHDOG/README.md) — estados, limites e critérios operacionais.
- [Registo dos consumidores](https://github.com/carlos-andrade/GOVERNANCA/blob/main/registry/repositorios-consumidores.json) — LICITACAO não estava listado como consumidor ativo na revisão.

## Estado dos controlos locais

| Controlo | Estado inicial | Ação exigida |
|---|---|---|
| Repositório acessível | PASS | Consultas públicas responderam |
| README e referências locais | EM_REVISAO | Revisar links e escopo nesta branch |
| Constituição/carta/roadmap | PENDENTE | Rever cabeçalhos, links e aprovar formalmente |
| Scorecard canónico | PENDENTE | Executar testes de esquema, pesos e evidências |
| WATCHDOG local | UNKNOWN | Executar validador e rever sistema/controlos declarados |
| CI do bootstrap executada com sucesso | PASS (escopo do workflow) | Execução [39449489411](https://github.com/carlos-andrade/LICITACAO/actions/runs/39449489411), commit `965d1a2993e49cd5b0ae7a4dacca84226bb2e379`; não certifica adoção ou conformidade integral |
| Proteção de branch | UNKNOWN | Verificar/configurar regras no GitHub |
| Supervisão externa independente | UNKNOWN | Ainda não implementada; exige integração e teste |
| Propagação automática da GOVERNANCA | BLOQUEADO/UNKNOWN | O mestre registou falha anterior de autenticação do token; revalidar secret sem o expor |
| Adoção formal | EM_REVISAO | Revisão e aprovação de pessoa autorizada pendentes |

## Decisão

**Não declarar a governança ativada/concluída neste momento.** O pacote local está em preparação. Para completar a adoção: concluir a revisão dos ficheiros, obter aprovação formal, confirmar/configurar revisão e proteção conforme as permissões disponíveis, inspecionar e testar WATCHDOG e validar a propagação upstream de ponta a ponta.

## Limite da inspeção

Não foi feita alteração ao repositório-mestre GOVERNANCA. O manifesto local identifica a origem e a política PR-only; não constitui espelho completo dos ficheiros canónicos nem prova de sincronização automática.

## Próxima ação

Rever esta preparação numa Pull Request; não fazer merge automático nem iniciar a estrutura funcional antes de concluir o gate de governança.
