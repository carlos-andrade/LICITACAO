# Carta/Contrato local — Adoção do padrão de roadmap

| Campo | Valor |
|---|---|
| **ID** | LIC-GOV-CARTA-ROADMAP-001 |
| **Projeto** | LICITACAO |
| **Repositório** | [carlos-andrade/LICITACAO](https://github.com/carlos-andrade/LICITACAO) |
| **Tipo documental** | CARTA_CONTRATO |
| **Fase** | Adoção de governança |
| **Estado** | APROVADO_COM_LIMITACOES |
| **Versão** | 0.1.2 |
| **SHA-256 (conteúdo canónico)** | PENDENTE — calcular após validação final do conteúdo |
| **Commit de referência (versão anterior)** | [f42637de27d382049109e30bb7f05008815d45ef](https://github.com/carlos-andrade/LICITACAO/commit/f42637de27d382049109e30bb7f05008815d45ef) |
| **Data de criação** | 2026-10-20 |
| **Data de atualização** | 2026-10-21 |
| **Responsável** | Proprietário do repositório LICITACAO |
| **Aprovador** | Carlos Andrade — decisão de adoção registada em 2026-10-21 |
| **Origem** | Adaptação local da Carta/Contrato canónica da GOVERNANCA |
| **Autoridade superior** | [Constituição local](CONSTITUICAO.md) e [Carta/Contrato canónico](https://github.com/carlos-andrade/GOVERNANCA/blob/main/CARTA-CONTRATO-PADRAO-ROADMAP.md) |
| **Cadeia de autoridade** | PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO |

## 1. Objeto

Esta carta formaliza a adoção local do padrão de roadmap da GOVERNANCA no LICITACAO, com as limitações registadas nesta carta e na inspeção de adoção. O roadmap é instrumento de decisão e auditoria, não lista informal de tarefas. Esta cópia local não substitui a fonte canónica nem representa certificação de conformidade total.

## 2. Requisitos mínimos

O roadmap deverá conter painel executivo, sequência de gates, ações prioritárias, dependências, riscos, bloqueios, decisões pendentes, exceções, evidências verificáveis, critérios de aceitação e histórico de alterações. O README deverá ligar ao roadmap e ao registo de status.

O percentual deve cumprir a [norma canónica de status](https://github.com/carlos-andrade/GOVERNANCA/blob/main/standards/status-e-percentual-de-conclusao.md) e derivar de fonte canónica validável. Não inferir conclusão pela mera criação de ficheiros.

## 3. Fail-closed

Não declarar fase concluída apenas porque um ficheiro foi criado ou código escrito. Não declarar teste executado sem resultado verificável, nem percentagem sem critérios pontuados e evidências. Dependências críticas desconhecidas mantêm o estado bloqueado ou aguardando evidência.

Exceções exigem regra afetada, motivo, risco, controlo compensatório, aprovador, validade e condição de revogação. Nenhuma exceção pode autorizar incumprimento de lei, edital ou contrato.

## 4. Responsabilidades

- Proprietário do repositório: aprovar escopo, risco e conclusão.
- Responsável do projeto: manter roadmap e evidências.
- Responsável técnico: assegurar verificações e rastreabilidade.
- Revisor: avaliar evidências e exceções quando necessário.

Papéis não nomeados permanecem pendentes; não inventar responsáveis.

## 5. Critérios de adoção

- [x] Constituição local e referências canónicas publicadas.
- [x] Roadmap local publicado e ligado no README.
- [x] Status com critérios, pontuação e evidências.
- [x] Gates G0–G6 mapeados para o ciclo LICITACAO.
- [x] Riscos, bloqueios e próxima ação documentados.
- [x] Inventário WATCHDOG local criado e validado documentalmente; os controlos operacionais não comprovados permanecem UNKNOWN.
- [x] Validação automatizada executada com resultado acessível ([CI pós-merge](https://github.com/carlos-andrade/LICITACAO/actions/runs/39623794138)).
- [x] Inspeção local registada e aprovada com limitações explícitas.

## 6. Estado

Estado atual: **APROVADO_COM_LIMITACOES** em 2026-10-21. A distribuição normativa está validada (79/79 Git blob SHA coincidentes) e a CI pós-merge concluiu com sucesso. O WATCHDOG não está operacional: sete controlos permanecem UNKNOWN. Esta aprovação autoriza a inclusão no âmbito de distribuição, não certificação operacional nem implementação funcional sem aprovação dos gates seguintes.

## 7. Histórico

| Versão | Data | Alteração | Evidência |
|---|---|---|---|
| 0.1.0 | 2026-10-20 | Criação inicial da carta de adoção local | Commit de preparação |
| 0.1.1 | 2026-10-20 | Normalização da carta para aplicação local | Branch de adoção; validação pendente |
| 0.1.2 | 2026-10-21 | Aprovação da adoção com limitações e evidência de CI/distribuição | PR #24 integrada; 79/79 hashes e CI pós-merge PASS |
