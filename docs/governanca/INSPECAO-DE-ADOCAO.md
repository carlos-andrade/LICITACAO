# Inspeção de adoção da GOVERNANCA — LICITACAO

| Campo | Valor |
|---|---|
| **ID** | LIC-GOV-INSPEC-001 |
| **Projeto** | LICITACAO |
| **Repositório** | [carlos-andrade/LICITACAO](https://github.com/carlos-andrade/LICITACAO) |
| **Tipo documental** | RELATORIO_DE_INSPECAO |
| **Fase** | Adoção de governança — revalidação |
| **Estado** | EM_REVISAO |
| **Versão** | 0.3.0 |
| **Data de atualização** | 2026-10-21 |
| **Responsável** | Pendente de nomeação formal no registo do projeto |
| **Aprovador** | Pendente |
| **Autoridade superior** | [GOVERNANCA/CONSTITUICAO.md](https://github.com/carlos-andrade/GOVERNANCA/blob/main/CONSTITUICAO.md) |
| **Cadeia de autoridade** | PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO |

## Resultado executivo

A revalidação confirma que o ruleset protect-main está ativo na branch predefinida e exige o check de estado validate. A execução de CI conhecida terminou com sucesso no commit de referência. Estes factos corrigem a inspeção anterior, que refletia o estado anterior à ativação do ruleset.

**Resultado global: EM_REVISAO; Gate G0 aprovado para entrada/planeamento.** A adoção global continua pendente da revisão e integração da distribuição documental completa (PR #23), dos checks pós-merge e do registo da checklist WATCHDOG. A proteção técnica e CI verde não provam adoção integral. A avaliação G0 foi atualizada em `docs/governanca/GATE-G0-AVALIACAO.md`; a autorização para ativar o repositório continua condicionada à validação da distribuição e dos controlos locais.

## Evidências verificadas

- Ruleset ativo: [protect-main — ID 25512579](https://github.com/carlos-andrade/LICITACAO/rules/25512579). A leitura da API em 2026-10-21 confirmou enforcement active, alvo ~DEFAULT_BRANCH, revisão obrigatória de uma pessoa, resolução de conversas e check obrigatório validate (integration_id 15368).
- CI de referência: [workflow run 39512218234](https://github.com/carlos-andrade/LICITACAO/actions/runs/39512218234), conclusão success, commit 7c236b33212d310a3787398a328104b59ffc86d0. Este run ocorreu em push para a branch principal; é evidência do workflow executado, não prova de que todas as futuras alterações passaram pelo check obrigatório.
- Registo canónico da GOVERNANCA: [repositorios-consumidores.json](https://github.com/carlos-andrade/GOVERNANCA/blob/main/registry/repositorios-consumidores.json). LICITACAO consta do registo com enabled: false; a própria nota do registo condiciona a ativação à aprovação individual e validação operacional da distribuição por PR.
- Constituição: [G0 — Entrada](https://github.com/carlos-andrade/GOVERNANCA/blob/main/CONSTITUICAO.md), que exige problema, beneficiário, patrocinador e responsável identificados.
- Carta/Contrato e roadmap padrão: [Carta](https://github.com/carlos-andrade/GOVERNANCA/blob/main/CARTA-CONTRATO-PADRAO-ROADMAP.md) e [Roadmap](https://github.com/carlos-andrade/GOVERNANCA/blob/main/ROADMAP-PADRAO-GOVERNANCA.md), que exigem inspeção local, critérios objetivos e evidências verificáveis.

## Estado dos controlos locais

| Controlo | Estado revalidado | Evidência / ação |
|---|---|---|
| Repositório acessível | PASS | Repositório público acessível pela API do GitHub. |
| Ruleset da branch principal | PASS | Ruleset protect-main ativo, ID 25512579; revisão e resolução de conversas exigidas. |
| Check de CI obrigatório | PASS (configuração) | Contexto validate presente em required_status_checks; confirmar execução em cada PR. |
| CI executado | PASS (escopo limitado) | Run 39512218234 concluído com sucesso; não certifica adoção integral. |
| Constituição/carta/roadmap e mapeamento local | EM_REVISAO | Rever consistência documental e obter aceitação formal. |
| Scorecard canónico | EM_REVISAO | Pontuação mantém-se a zero até validação e aceitação formal de critérios com evidências. |
| WATCHDOG local | EM_REVISAO | LIC-WD-006 corrigido para PASS; os restantes controlos UNKNOWN/PENDENTES exigem execução ou integração real. |
| Supervisão externa independente | UNKNOWN | Não demonstrada por evidência operacional. |
| Distribuição upstream por PR | BLOQUEADO/PENDENTE | LICITACAO continua enabled: false no registo-mestre; validar fluxo operacional antes de pedir ativação. |
| Adoção formal da GOVERNANCA | EM_REVISAO | Depende da inspeção, aprovação autorizada e validação operacional da distribuição por PR. |
| Gate G0 — Entrada | BLOQUEADO | Problema/resultado esperado, beneficiário, patrocinador e responsável formal ainda não estão todos documentados e aprovados num registo de entrada. |

## Gate G0 — avaliação

O registo de avaliação está em [GATE-G0-AVALIACAO.md](GATE-G0-AVALIACAO.md). O estado é **BLOQUEADO / AGUARDANDO EVIDÊNCIA**. Não atribuir aprovação implícita com base nesta revalidação técnica.

## Decisão e limites

1. Atualizar os registos não equivale a aprovar a adoção da GOVERNANCA.
2. Não alterar o registo-mestre para enabled: true enquanto a aprovação individual e o teste de distribuição por PR não estiverem comprovados.
3. Não iniciar a estrutura funcional do produto enquanto G0 não estiver aprovado.
4. A proteção técnica foi verificada via ruleset API. A leitura do endpoint clássico de branch protection não foi usada como prova, pois não estava acessível pela integração; o ruleset é a evidência autoritativa disponível para esta verificação.
5. O CI atual valida apenas o que está implementado no workflow. Não substitui revisão independente, validação de WATCHDOG nem aceitação formal.

## Próximas ações

1. Completar o registo G0 com problema, resultado, beneficiário, patrocinador, responsável, escopo inicial, riscos/dependências e critérios de aceitação.
2. Obter aprovação explícita do Gate G0 por pessoa autorizada.
3. Testar o fluxo de distribuição da GOVERNANCA por Pull Request sem merge automático e recolher evidência.
4. Após os passos anteriores, solicitar a ativação de LICITACAO no registo-mestre por PR.
5. Só após G0 aprovado, iniciar a estrutura funcional; manter a política de PR e CI obrigatório.

## Histórico

| Versão | Data | Alteração | Evidência |
|---|---|---|---|
| 0.1.0 | 2026-10-20 | Inspeção inicial, com proteção da branch ainda não ativada | Commit de referência anterior |
| 0.2.0 | 2026-10-21 | Ruleset e check obrigatório revalidados; Gate G0 formalizado como bloqueado até haver evidência e aprovação | [Ruleset](https://github.com/carlos-andrade/LICITACAO/rules/25512579), [CI](https://github.com/carlos-andrade/LICITACAO/actions/runs/39512218234) |

## Revalidação complementar — 2026-10-21

- G0: aprovado para entrada/planeamento com problema, resultado mensurável, beneficiários, papéis, escopo, exclusões, riscos e critérios documentados na avaliação atualizada.
- Distribuição upstream: [PR #23](https://github.com/carlos-andrade/LICITACAO/pull/23) contém 79 ficheiros de texto dos diretórios publicados; comparação pré-PR confirmou 79/79 Git blob SHA coincidentes. O check obrigatório `validate` está atualmente em fila, pelo que não há ainda resultado CI final nem validação pós-merge.
- WATCHDOG: controlos obrigatórios locais permanecem `UNKNOWN`; a checklist de adoção operacional ainda precisa de execução e evidência. Não declarar WATCHDOG operacional.
- Registo-mestre: `LICITACAO.enabled=false` deve ser preservado até a distribuição ser integrada e validada e a adoção individual receber aprovação formal.

- Checklist WATCHDOG executada documentalmente: [CHECKLIST-WATCHDOG-ADOPCAO.md](CHECKLIST-WATCHDOG-ADOPCAO.md). Resultado: 1 controlo PASS por evidência direta e 7 UNKNOWN; WATCHDOG não operacional.
