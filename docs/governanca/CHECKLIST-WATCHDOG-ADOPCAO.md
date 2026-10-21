# Checklist de adoção WATCHDOG — LICITACAO

| Campo | Valor |
|---|---|
| **ID** | LIC-WD-CHECKLIST-001 |
| **Data de execução documental** | 2026-10-21 |
| **Estado** | EXECUTADA — WATCHDOG NÃO OPERACIONAL |
| **Responsável pelo registo** | Carlos Andrade, conforme registo do projeto |
| **Escopo** | Revisão documental e evidências disponíveis; não equivale a teste de produção |

## Resultados

| ID | Controlo | Resultado | Evidência / lacuna |
|---|---|---|---|
| LIC-WD-COV-001 | Inventário de sistemas com proprietário e criticidade | PASS | [Inventário](../../WATCHDOG/registry/sistemas-monitorizados.json): sistema `LICITACAO-REPO`, proprietário Carlos Andrade, criticidade `high`. |
| LIC-WD-COV-002 | Evidência rastreável para cada PASS | UNKNOWN | É necessário validar a rastreabilidade de todos os controlos marcados PASS por uma execução independente. |
| LIC-WD-COV-003 | Dados ou execuções ausentes nunca classificados como PASS | UNKNOWN | Princípio documentado; falta teste negativo automatizado que demonstre o comportamento fail-closed. |
| LIC-WD-COV-004 | Responsável, canal de alerta e escalonamento definidos | UNKNOWN | Responsável do projeto identificado; canal de alerta, SLA e escalonamento operacional não comprovados. |
| LIC-WD-COV-005 | Supervisão independente do próprio monitor | UNKNOWN | Monitor externo independente não implementado nem testado. |
| LIC-WD-COV-006 | Teste de falha e recuperação para controlos críticos | UNKNOWN | Não foi apresentada evidência de teste de falha/recuperação executado. |
| LIC-WD-COV-007 | Proteção de segredos e informações comerciais | UNKNOWN | Política documentada, mas falta resultado de ferramenta de secret scanning arquivado e verificável. |
| LIC-WD-COV-008 | Revisão de mudanças por pull request | UNKNOWN | O fluxo usa PR e o ruleset exige `validate`; não há evidência suficiente de revisão independente obrigatória para todas as mudanças. |

## Decisão

A checklist foi executada no âmbito documental. Apenas o controlo de inventário recebeu PASS, por evidência direta. Os restantes permanecem UNKNOWN; não foram convertidos em PASS por inferência.

**O WATCHDOG não é declarado operacional.** Os controlos UNKNOWN são limitações abertas e devem ser fechados com testes/evidências antes de qualquer declaração de operação contínua. Esta checklist não substitui a aprovação individual da adoção nem a validação pós-merge da distribuição upstream.

## Referências

- [Registo de controlos obrigatórios](../../WATCHDOG/registry/controlos-obrigatorios.json)
- [Inventário de sistemas monitorizados](../../WATCHDOG/registry/sistemas-monitorizados.json)
- [PR #23 — distribuição upstream](https://github.com/carlos-andrade/LICITACAO/pull/23)
- [Avaliação G0](GATE-G0-AVALIACAO.md)
