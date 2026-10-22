# Inspeção de adoção da GOVERNANCA — LICITACAO

| Campo | Valor |
|---|---|
| **ID** | LIC-GOV-INSPEC-001 |
| **Projeto** | LICITACAO |
| **Repositório** | [carlos-andrade/LICITACAO](https://github.com/carlos-andrade/LICITACAO) |
| **Tipo documental** | RELATORIO_DE_INSPECAO |
| **Fase** | Adoção de governança — decisão |
| **Estado** | EM_REVISAO |
| **Versão** | 0.4.1 |
| **SHA-256 (conteúdo canónico)** | 0fc7333ff910963acf660fe2998886f16791b21eec833dcd5ce93dd5dacbfe33 |
| **Commit de referência (versão anterior)** | [b5e445630ceaf57fac58ae963dbedc587d836e52](https://github.com/carlos-andrade/LICITACAO/commit/b5e445630ceaf57fac58ae963dbedc587d836e52) |
| **Data de criação** | N/A — data histórica não verificada |
| **Data de atualização** | 2026-10-22 |
| **Responsável** | Carlos Andrade, conforme registo-mestre |
| **Aprovador** | Carlos Andrade — decisão de adoção registada em 2026-10-21 |
| **Origem** | Conteúdo existente no repositório; caminho: `docs/governanca/INSPECAO-DE-ADOCAO.md` |
| **Autoridade superior** | [GOVERNANCA/CONSTITUICAO.md](https://github.com/carlos-andrade/GOVERNANCA/blob/main/CONSTITUICAO.md) |
| **Cadeia de autoridade** | PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO |

## 1. Decisão executiva

**Resultado global: APROVADO_COM_LIMITACOES. Gate G0: APROVADO.**

A adoção documental foi aprovada com limitações explícitas. A distribuição normativa completa foi integrada pela [LICITACAO PR #24](https://github.com/carlos-andrade/LICITACAO/pull/24); a verificação pós-merge confirmou 79/79 Git blob SHA coincidentes com a origem, sem divergências, e o check `validate` concluiu com sucesso na [execução pós-merge 39623794138](https://github.com/carlos-andrade/LICITACAO/actions/runs/39623794138).

A checklist WATCHDOG foi executada e registada em [CHECKLIST-WATCHDOG-ADOPCAO.md](CHECKLIST-WATCHDOG-ADOPCAO.md): 1 controlo PASS por evidência direta e 7 UNKNOWN. **O WATCHDOG não é declarado operacional.** Os estados UNKNOWN permanecem limitações e não podem ser apresentados como PASS.

## 2. Evidências verificadas

- **G0:** [GATE-G0-AVALIACAO.md](GATE-G0-AVALIACAO.md) documenta problema, resultado mensurável, beneficiários, patrocinador/responsável, escopo, exclusões, riscos e critérios iniciais.
- **Scorecard:** [status-do-projeto.json](../../registry/status-do-projeto.json) regista 20/20 pontos para os critérios da fase de entrada, com referências de evidência.
- **Distribuição upstream:** [PR #24](https://github.com/carlos-andrade/LICITACAO/pull/24) integrada; comparação pós-merge 79/79 SHA coincidentes.
- **CI:** [run 39623794138](https://github.com/carlos-andrade/LICITACAO/actions/runs/39623794138), check `validate` concluído com sucesso.
- **Ruleset:** [protect-main](https://github.com/carlos-andrade/LICITACAO/rules/25512579) ativo e com check obrigatório `validate`.
- **WATCHDOG:** [checklist executada](CHECKLIST-WATCHDOG-ADOPCAO.md), 1 PASS e 7 UNKNOWN; monitorização operacional não comprovada.
- **Ativação central:** [GOVERNANCA PR #32](https://github.com/carlos-andrade/GOVERNANCA/pull/32) propõe `LICITACAO.enabled=true), mas permanece em rascunho até esta inspeção e a decisão de ativação estarem integradas e verificadas.

## 3. Estado por controlo

| Controlo | Estado | Evidência / limitação |
|---|---|---|
| Constituição/carta/roadmap e mapeamento local | APROVADO_COM_LIMITACOES | Documentação alinhada; gates seguintes continuam aplicáveis. |
| Scorecard da fase de entrada | PASS | 20/20 pontos com evidências ligadas; progresso de fases posteriores permanece 0. |
| Distribuição upstream por PR | PASS | 79/79 hashes iguais após merge; CI pós-merge PASS. |
| Ruleset e CI | PASS | Ruleset ativo; check `validate` obrigatório e execução pós-merge verde. |
| Inventário de sistemas | PASS | Repositório identificado com owner Carlos Andrade e criticidade `high`. |
| Evidência rastreável para cada PASS | UNKNOWN | Falta validação independente de toda a cadeia de evidências. |
| Fail-closed perante dados/testes ausentes | UNKNOWN | Princípio documentado; teste negativo automatizado ainda não comprovado. |
| Canal de alertas e escalonamento | UNKNOWN | Responsável identificado; canal/SLA operacional não demonstrados. |
| Supervisão independente | UNKNOWN | Monitor externo independente não implementado/testado. |
| Teste de falha e recuperação | UNKNOWN | Sem evidência de teste executado. |
| Secret scanning | UNKNOWN | Política documentada; resultado de ferramenta de scanning não arquivado. |
| Revisão independente de mudanças | UNKNOWN | Fluxo por PR existe; evidência de revisão independente em todas as alterações não demonstrada. |

## 4. Limites da aprovação

Esta aprovação cobre a adoção documental e a distribuição das normas. Não significa:

- certificação de conformidade jurídica ou fiscal;
- WATCHDOG operacional;
- aplicação de negócio implementada;
- autorização para submissão automática de propostas/lances;
- aprovação dos gates G1–G6.

A próxima fase de projeto é G1 — viabilidade. A implementação funcional depende dos gates e critérios aplicáveis.

## 5. Decisão e ativação

- **Decisão de adoção:** APROVADO_COM_LIMITACOES em 2026-10-21.
- **Aprovador:** Carlos Andrade, conforme registo-mestre e instrução explícita de regularização.
- **Registo-mestre efetivo:** `LICITACAO.enabled=true` desde a [GOVERNANCA PR #32](https://github.com/carlos-andrade/GOVERNANCA/pull/32). A ativação não equivale a certificação operacional.
- **Condição de ativação:** manter limitações WATCHDOG visíveis e não declarar controlo operacional sem evidência.
