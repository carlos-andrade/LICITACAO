# Avaliação do Gate G0 — Entrada do projeto LICITACAO

| Campo | Valor |
|---|---|
| **ID** | LIC-G0-001 |
| **Projeto** | LICITACAO |
| **Gate** | G0 — Entrada |
| **Estado** | BLOQUEADO / AGUARDANDO EVIDÊNCIA |
| **Data da avaliação** | 2026-10-21 |
| **Autoridade normativa** | [Constituição da GOVERNANCA, secção 5](https://github.com/carlos-andrade/GOVERNANCA/blob/main/CONSTITUICAO.md) |
| **Inspeção associada** | [INSPECAO-DE-ADOCAO.md](INSPECAO-DE-ADOCAO.md) |

## Critérios de entrada

A Constituição da GOVERNANCA define G0 como a confirmação de problema, beneficiário, patrocinador e responsável identificados. A existência de repositório, regras de proteção ou CI não satisfaz automaticamente esses critérios.

| Critério | Estado | Evidência atual / lacuna |
|---|---|---|
| Problema a resolver e resultado verificável | PENDENTE | A descrição do repositório refere genericamente licitações públicas; falta declarar o problema operacional específico e o resultado esperado. |
| Beneficiário(s) identificados | PENDENTE | Não há beneficiários e necessidades identificados neste registo. |
| Patrocinador identificado | PENDENTE | Não há nomeação explícita neste registo. |
| Responsável/owner do projeto identificado | PENDENTE | Os registos atuais declaram que a nomeação formal está pendente. |
| Escopo inicial e exclusões | PENDENTE | Não documentados e aceites. |
| Riscos, dependências e obrigações aplicáveis | PENDENTE | Exige levantamento inicial; não presumir requisitos legais, operacionais ou técnicos. |
| Critérios de aceitação e plano inicial | PENDENTE | Não definidos e aprovados. |
| Aprovação explícita de G0 | NÃO APROVADO | Não existe evidência de aprovação formal do gate. |

## Evidências técnicas já verificadas (não substituem G0)

- Ruleset [protect-main](https://github.com/carlos-andrade/LICITACAO/rules/25512579) ativo; exige uma aprovação, resolução de conversas e check de estado validate.
- [Execução de CI 39512218234](https://github.com/carlos-andrade/LICITACAO/actions/runs/39512218234) concluída com sucesso no commit 7c236b33212d310a3787398a328104b59ffc86d0.
- O registo-mestre da GOVERNANCA mantém LICITACAO com enabled: false, até aprovação individual e validação operacional da distribuição por PR: [registo de consumidores](https://github.com/carlos-andrade/GOVERNANCA/blob/main/registry/repositorios-consumidores.json).

## Condições para desbloqueio

1. Registar o problema, o resultado esperado e como serão medidos.
2. Identificar beneficiários e necessidades.
3. Nomear expressamente patrocinador e responsável do projeto.
4. Delimitar escopo inicial, exclusões, dependências, riscos e obrigações relevantes.
5. Definir critérios de aceitação objetivos e plano inicial.
6. Obter aprovação explícita do Gate G0 e guardar a evidência verificável no repositório.
7. Concluir a inspeção individual da GOVERNANCA e demonstrar a distribuição upstream por Pull Request antes de solicitar enabled: true no repositório-mestre.

## Decisão fail-closed

**G0 permanece BLOQUEADO. Não iniciar a estrutura funcional nem criar módulos de negócio enquanto os critérios acima não estiverem documentados e aprovados.** Esta decisão evita inventar patrocinador, beneficiários, requisitos ou aceitação que não foram fornecidos.

## Registo de decisão

- Decisão atual: AGUARDANDO_EVIDENCIA.
- Aprovador: pendente.
- Data de aprovação: não aplicável.
- Evidência de aprovação: inexistente.