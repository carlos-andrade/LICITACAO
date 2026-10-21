# Plano de regularização do Gate G0 — LICITACAO

| Campo | Valor |
|---|---|
| **ID** | LIC-G0-PLANO-001 |
| **Projeto** | LICITACAO |
| **Tipo documental** | PLANO_DE_REGULARIZACAO |
| **Estado** | ADOÇÃO DOCUMENTAL APROVADA_COM_LIMITACOES; ATIVAÇÃO CENTRAL EFETIVA |
| **Versão** | 0.1.0 |
| **Data** | 2026-10-21 |
| **Gate relacionado** | [GATE-G0-AVALIACAO.md](GATE-G0-AVALIACAO.md) |
| **Issue de acompanhamento** | [LICITACAO #6](https://github.com/carlos-andrade/LICITACAO/issues/6) |
| **Regra de segurança** | Fail-closed; não altera `enabled: false` |

## 1. Objetivo

Consolidar a regularização documental do Gate G0 e controlar os requisitos remanescentes de adoção. A entrada/planeamento foi aprovada em 2026-10-21; este documento não ativa o repositório nem autoriza implementação funcional antes da validação da adoção global.

## 2. Estado de partida verificado

- O Gate G0 está aprovado para entrada/planeamento com base na avaliação atualizada em `GATE-G0-AVALIACAO.md`. A adoção documental está aprovada com limitações após a distribuição completa e a CI pós-merge. Os controlos WATCHDOG sem evidência permanecem UNKNOWN; a ativação central foi efetivada pela GOVERNANCA PR #32.
- O registo-mestre da GOVERNANCA mantém LICITACAO com `enabled: false`.
- A proteção da branch e a CI são controlos técnicos; não substituem a aprovação de negócio nem a adoção formal da GOVERNANCA.
- O WATCHDOG local ainda tem controlos obrigatórios em `UNKNOWN`; a presença do inventário não demonstra operação contínua.

## 3. Ficha de decisão G0 — preencher sem inventar dados

### 3.1 Problema e resultado

- **Problema operacional específico a resolver:** [PREENCHER]
- **Como o problema é resolvido atualmente e qual a limitação:** [PREENCHER]
- **Resultado esperado verificável:** [PREENCHER]
- **Métrica, linha de base e meta:** [PREENCHER]
- **Fonte da evidência para medir o resultado:** [PREENCHER]

### 3.2 Pessoas e partes interessadas

- **Beneficiário(s) e respetivas necessidades:** [PREENCHER]
- **Patrocinador — nome/entidade e autoridade para aprovar:** [PREENCHER]
- **Responsável formal pelo projeto — nome/entidade e responsabilidades:** [PREENCHER]
- **Aprovador do Gate G0:** [PREENCHER]
- **Conflitos de interesse ou separação de funções necessária:** [PREENCHER OU JUSTIFICAR N/A]

Não inferir que o proprietário do repositório é automaticamente patrocinador, responsável formal ou aprovador. Cada papel deve ser confirmado expressamente.

### 3.3 Escopo inicial

- **Incluído na primeira entrega:** [PREENCHER]
- **Excluído da primeira entrega:** [PREENCHER]
- **Utilizadores e perfis previstos:** [PREENCHER]
- **Fontes de dados e integrações previstas:** [PREENCHER]
- **Dependências internas/externas:** [PREENCHER]
- **Dados pessoais, confidenciais ou comerciais potencialmente tratados:** [PREENCHER]
- **Obrigações legais, regulamentares, contratuais e de arquivo a avaliar:** [PREENCHER; não presumir conformidade]
- **Riscos iniciais, mitigação e responsável por cada risco:** [PREENCHER]

### 3.4 Critérios de aceitação e plano

Definir critérios objetivos, verificáveis e associados a evidências. Para cada critério, indicar método de teste, resultado esperado, responsável e localização da evidência.

| ID | Critério de aceitação | Método/evidência | Responsável | Estado |
|---|---|---|---|---|
| AC-01 | O problema e o resultado mensurável estão documentados e aceites | Documento aprovado e métrica definida | PENDENTE | PENDENTE |
| AC-02 | Beneficiários e necessidades estão identificados | Registo validado | PENDENTE | PENDENTE |
| AC-03 | Patrocinador e responsável formal estão nomeados | Decisão explícita e rastreável | PENDENTE | PENDENTE |
| AC-04 | Escopo, exclusões, dependências e riscos estão aprovados | Escopo e registo de riscos revistos | PENDENTE | PENDENTE |
| AC-05 | Obrigações relevantes foram avaliadas, com lacunas registadas | Avaliação documentada; revisão especializada quando necessária | PENDENTE | PENDENTE |
| AC-06 | Plano inicial tem entregáveis, sequência e critérios de saída | Roadmap aprovado | PENDENTE | PENDENTE |
| AC-07 | A adoção individual da GOVERNANCA tem evidências suficientes | Inspeção atualizada e controlos validados | PENDENTE | PENDENTE |
| AC-08 | Distribuição upstream por PR foi demonstrada de ponta a ponta | PR, checks e evidência de sincronização | PENDENTE | PENDENTE |
| AC-09 | A decisão de G0 foi explicitamente aprovada | Registo de decisão aprovado | PENDENTE | PENDENTE |

## 4. Sequência de execução

1. **Recolher as decisões em falta.** O patrocinador e o responsável formal devem ser indicados explicitamente; documentar o problema, os beneficiários, o resultado e as métricas.
2. **Consolidar o escopo.** Registar inclusões/exclusões, dependências, riscos e obrigações a avaliar. Marcar desconhecidos como pendentes, não como conformes.
3. **Aprovar os critérios de aceitação e o plano inicial.** A aprovação deve ser identificável e rastreável.
4. **Concluir a inspeção da GOVERNANCA.** Revalidar os controlos WATCHDOG, corrigir divergências documentais e obter evidências atuais dos testes.
5. **Demonstrar a distribuição upstream por Pull Request.** Registar PR, revisão, checks, resultado e comparação de conteúdos; a coincidência parcial de ficheiros não basta para provar o fluxo completo.
6. **G0 concluído para entrada/planeamento.** A decisão está registada em `GATE-G0-AVALIACAO.md`; não confundir esta decisão com adoção global aprovada.
7. **Só após todas as condições remanescentes serem satisfeitas**, solicitar a ativação individual de LICITACAO no registo-mestre da GOVERNANCA através do processo autorizado. Não editar `enabled` como substituto da aprovação.

## 5. Condições de bloqueio

G0 continua bloqueado se ocorrer qualquer uma destas situações:

- papel obrigatório sem nomeação explícita;
- problema, resultado ou métrica ambíguos;
- escopo, riscos ou critérios de aceitação incompletos;
- evidência técnica ausente, desatualizada ou não reproduzível;
- adoção individual ou distribuição upstream sem validação ponta a ponta;
- aprovação formal inexistente;
- divergência entre documentação, estado do repositório e registo-mestre.

## 6. Registo de decisão

- **Decisão:** G0 APROVADO; ADOÇÃO DOCUMENTAL APROVADO_COM_LIMITACOES; ATIVAÇÃO CENTRAL PENDENTE.
- **Estado do Gate G0:** APROVADO.
- **Aprovador / patrocinador:** Carlos Andrade, conforme registo-mestre e instrução explícita de regularização.
- **Data da decisão:** 2026-10-21.
- **Evidência de aprovação:** decisão registada em `GATE-G0-AVALIACAO.md`.
- **Estado de ativação:** manter `enabled: false`.
- **Autorização para iniciar módulos funcionais:** NÃO CONCEDIDA.

## 7. Histórico

- 2026-10-21 — Criado plano de regularização para tornar explícitas as lacunas e a sequência de validação. Nenhum critério foi marcado como aprovado sem evidência.
