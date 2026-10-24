# WATCHDOG local — LICITACAO

| Campo | Valor |
|---|---|
| **ID** | LIC-GOV-WD-README-001 |
| **Projeto** | LICITACAO |
| **Repositório** | [carlos-andrade/LICITACAO](https://github.com/carlos-andrade/LICITACAO) |
| **Tipo documental** | PROCEDIMENTO |
| **Fase** | Adoção de governança |
| **Estado** | EM_REVISAO |
| **Versão** | 0.1.0 |
| **SHA-256 (conteúdo canónico)** | 87e454346a59c58c2ea61ea632dcf4bc7fa73ed5b7341365d8cfa14bbbcc82a1 |
| **Commit de referência (versão anterior)** | [f42637de27d382049109e30bb7f05008815d45ef](https://github.com/carlos-andrade/LICITACAO/commit/f42637de27d382049109e30bb7f05008815d45ef) |
| **Data de criação** | 2026-10-20 |
| **Data de atualização** | 2026-10-24 |
| **Responsável** | Proprietário do repositório LICITACAO |
| **Aprovador** | Pendente de aprovação formal |
| **Origem** | Adaptação inicial do [WATCHDOG da GOVERNANCA](https://github.com/carlos-andrade/GOVERNANCA/tree/main/WATCHDOG) |
| **Autoridade superior** | [Constituição local](../CONSTITUICAO.md) e política canónica WATCHDOG |
| **Cadeia de autoridade** | PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO |

## Objetivo

Preparar um inventário local de sistemas e controlos antes da implementação da aplicação. A presença deste ficheiro não significa que monitorização contínua, alertas ou recuperação estejam operacionais.

## Estados dos controlos

- `PASS`: verificação executada, critério satisfeito e evidência ligada.
- `WARN`: condição degradada que exige avaliação.
- `FAIL`: condição verificada que viola o critério.
- `UNKNOWN`: não há dados suficientes, verificação não implementada ou monitor indisponível.

Ausência de dados ou de execução nunca equivale a PASS. Remediação automática fica desativada por defeito.

## Sistemas a monitorizar

Consultar [registry/sistemas-monitorizados.json](registry/sistemas-monitorizados.json) e [registry/controlos-obrigatorios.json](registry/controlos-obrigatorios.json). Owners funcionais permanecem pendentes até nomeação. Verificações externas e supervisão independente permanecem UNKNOWN até implementação e teste. A inspeção de adoção registada em 2026-10-21 reporta o ruleset `protect-main` ativo, com aprovação obrigatória, resolução de conversas e check `validate`. Esta evidência contradiz o registo histórico anterior de branch sem proteção; por isso, o estado do controlo de proteção deve ser revalidado na próxima execução e o resultado atual documentado com evidência datada. Não declarar o WATCHDOG operacional apenas com base na proteção da branch.

## Critério de adoção operacional

O WATCHDOG só pode ser declarado operacional quando o inventário estiver revisto, os controlos prioritários forem testados, adaptadores e alertas estiverem verificados, houver mecanismo independente para detetar falha do monitor, responsabilidades/escalonamento forem aprovados e evidências de recuperação forem registadas.

## Referência canónica

- [README WATCHDOG](https://github.com/carlos-andrade/GOVERNANCA/blob/main/WATCHDOG/README.md)
- [Política de monitorização](https://github.com/carlos-andrade/GOVERNANCA/blob/main/WATCHDOG/normas/politica-de-monitorizacao.md)
- [Controlos obrigatórios](https://github.com/carlos-andrade/GOVERNANCA/blob/main/WATCHDOG/registry/controlos-obrigatorios.json)
