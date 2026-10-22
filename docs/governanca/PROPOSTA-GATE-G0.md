# Proposta documental para desbloqueio do Gate G0 — LICITACAO

| Campo | Valor |
|---|---|
| **ID** | LIC-DOC-DOCS-GOVERNANCA-PROPOSTA-GATE-G0-MD-BE2E0033 |
| **Projeto** | LICITAÇÃO |
| **Repositório** | [carlos-andrade/LICITACAO](https://github.com/carlos-andrade/LICITACAO) |
| **Tipo documental** | DOCUMENTO_TECNICO |
| **Fase** | N/A — fase não definida no conteúdo de origem |
| **Estado** | EM_REVISAO |
| **Versão** | 1.0.0 |
| **SHA-256 (conteúdo canónico)** | 32d667904aa73c2f68f96737d81f5e358897f0ad4348a9021d2089ae8692c404 |
| **Commit de referência (versão anterior)** | [b5e445630ceaf57fac58ae963dbedc587d836e52](https://github.com/carlos-andrade/LICITACAO/commit/b5e445630ceaf57fac58ae963dbedc587d836e52) |
| **Data de criação** | N/A — data histórica não verificada |
| **Data de atualização** | 2026-10-22 |
| **Responsável** | Responsável pelo projeto LICITAÇÃO |
| **Aprovador** | Pendente — não há evidência de aprovação neste documento |
| **Origem** | Conteúdo existente no repositório; caminho: `docs/governanca/PROPOSTA-GATE-G0.md` |
| **Autoridade superior** | [Constituição do projeto](https://github.com/carlos-andrade/LICITACAO/blob/main/CONSTITUICAO.md) |
| **Cadeia de autoridade** | PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO |

- **ID:** LIC-G0-PROP-002
- **Estado:** PROPOSTA PARA REVISÃO — NÃO APROVADA
- **Gate:** G0 — Entrada do projeto
- **Data de preparação:** 2026-10-21
- **Projeto:** `carlos-andrade/LICITACAO`
- **Estado operacional obrigatório:** Gate G0 `BLOQUEADO / AGUARDANDO EVIDÊNCIA`; `LICITACAO.enabled=false`
- **Documento normativo relacionado:** [GATE-G0-AVALIACAO.md](GATE-G0-AVALIACAO.md)
- **Adoção da GOVERNANCA:** decisão separada; permanece sujeita à aprovação humana e à validação operacional da distribuição por PR.

> Este documento é uma proposta para recolher validação e evidências. Não representa aprovação do Gate G0, não confirma autoridade de aprovação, não altera o registo central da GOVERNANCA e não autoriza desenvolvimento de módulos funcionais.

## 1. Problema e resultado esperado

### Proposta de problema

Empresas que concorrem a concursos públicos precisam de organizar e avaliar oportunidades, requisitos dos procedimentos, documentação, custos, propostas, prazos e obrigações contratuais. A informação dispersa e a falta de rastreabilidade podem aumentar o esforço operacional, atrasar decisões e contribuir para omissões.

**A validar pelo patrocinador:** se esta descrição corresponde ao problema real a resolver, quais os processos prioritários e que evidência demonstra a dimensão do problema. Não há, nesta proposta, dados de base que permitam afirmar a frequência ou o impacto atual dessas dificuldades.

### Resultado esperado proposto

Definir e validar um processo rastreável para apoiar a identificação e qualificação de oportunidades públicas, análise de requisitos, preparação de propostas e acompanhamento das obrigações, mantendo decisões e submissões sob controlo humano.

A solução não deverá presumir elegibilidade, conformidade legal, sucesso de uma candidatura ou exatidão de informação sem verificação da fonte.

## 2. Beneficiários e partes interessadas

- **Beneficiário principal indicado:** empresas que concorrem a concursos públicos.
- **Utilizadores potenciais a confirmar:** responsáveis comerciais, equipas de propostas, especialistas técnicos, compras, jurídico/conformidade, operações e faturação.
- **Necessidades concretas:** pendentes de entrevistas, observação de processos ou outra evidência validada.
- **Segmento inicial e dimensão do grupo piloto:** pendentes.
- **Partes externas e integrações necessárias:** pendentes de levantamento.

## 3. Patrocínio e responsabilidade

| Função | Proposta atual | Estado |
|---|---|---|
| Patrocinador do projeto | Carlos Andrade | Indicado pelo solicitante; confirmação formal e mandato pendentes |
| Aprovador do Gate G0 | Carlos Andrade | Indicado pelo solicitante; autoridade para aprovar deve ser confirmada e registada |
| Responsável pelo projeto | Carlos Andrade | Indicado pelo solicitante; aceitação formal da responsabilidade pendente |
| Revisor independente da PR documental | Pessoa elegível diferente do autor | Pendente de identificação |
| Responsável por segurança, privacidade e conformidade | A designar conforme o escopo e a organização | Pendente |

A indicação de um nome não constitui por si só nomeação formal, comprovação de mandato nem aprovação do Gate. A aprovação deve ser registada de forma explícita e verificável, respeitando as regras do repositório. O autor não deve aprovar a própria PR.

## 4. Escopo inicial proposto

### Incluído na fase de descoberta e definição

1. Mapear o processo atual de gestão de oportunidades e preparação de propostas.
2. Identificar fontes de oportunidades e documentos oficiais que poderão ser consultados.
3. Definir requisitos funcionais e não funcionais prioritários.
4. Definir modelo de permissões, rastreabilidade, auditoria, retenção e proteção de dados.
5. Identificar integrações, custos operacionais, dependências e restrições.
6. Definir um piloto limitado e critérios de aceitação antes de qualquer implementação funcional.

### Exclusões propostas para a fase inicial

- Submissão automática de propostas ou tomada de decisão autónoma de bid/no-bid.
- Garantia automática de conformidade jurídica ou de elegibilidade.
- Assinatura, contratação, compromisso financeiro ou comunicação externa sem autorização humana.
- Implementação de módulos funcionais antes da aprovação formal de G0.
- Ativação do consumidor no registo central da GOVERNANCA.
- Distribuição upstream fora da política `pull_request_only`.

Estas exclusões são propostas e precisam de validação do patrocinador e das partes interessadas.

## 5. Critérios mensuráveis propostos

Os valores abaixo são **propostas de metas**, não resultados observados. A linha de base, a amostra e o método de medição devem ser definidos antes do piloto.

| ID | Critério proposto | Meta inicial proposta | Evidência exigida |
|---|---|---|---|
| G0-M01 | Processo prioritário documentado | 1 fluxo ponta a ponta validado por representantes dos utilizadores | Fluxo versionado e registo da validação |
| G0-M02 | Requisitos prioritários rastreáveis | 100% dos requisitos do piloto ligados a origem, responsável e teste de aceitação | Matriz de rastreabilidade |
| G0-M03 | Oportunidades de teste com fonte identificável | 100% das oportunidades da amostra com URL/documento de origem e data de consulta | Amostra reproduzível e relatório de teste |
| G0-M04 | Controlo humano | 100% das ações de submissão, compromisso ou comunicação externa exigem autorização humana explícita | Cenários de teste e evidência de revisão |
| G0-M05 | Rastreabilidade de decisões | 100% das decisões críticas do piloto registam ator, data, decisão e justificação | Registos de auditoria de teste |
| G0-M06 | Qualidade dos dados | Métrica de completude e taxa de erro definida antes do piloto; limiar aprovado pelo patrocinador | Relatório de qualidade com denominador e método |
| G0-M07 | Viabilidade operacional | Estimativa documentada de custos, dependências e esforço de manutenção antes da decisão de implementação | Avaliação técnica e operacional |
| G0-M08 | Segurança e privacidade | 100% dos riscos críticos identificados têm mitigação, responsável e decisão registados antes de dados reais | Avaliação de riscos aprovada |

Antes de transformar estas metas em critérios definitivos, definir: tamanho e seleção da amostra, linha de base, ferramentas de medição, tolerâncias, responsáveis por verificar os resultados e consequências de falha. Nenhuma métrica deve ser marcada como satisfeita sem evidência verificável.

## 6. Riscos, dependências e obrigações a avaliar

| Tema | Risco ou questão | Ação necessária | Estado |
|---|---|---|---|
| Fontes oficiais | Dados desatualizados, indisponíveis ou com termos de uso restritivos | Inventariar fontes, frequência de atualização e condições de acesso | Pendente |
| Conformidade | Requisitos legais e regras variam por procedimento e jurisdição | Identificar jurisdições e obter revisão competente; não presumir conformidade | Pendente |
| Dados pessoais/confidenciais | Tratamento excessivo, acesso indevido ou retenção inadequada | Mapear dados, base de tratamento aplicável, acessos e retenção | Pendente |
| Decisão comercial | Qualificação incorreta pode causar perda de oportunidade | Definir revisão humana, critérios e registo de decisão | Pendente |
| Segurança | Exposição de credenciais, documentos ou propostas | Definir modelo de ameaças, gestão de segredos e controlo de acesso | Pendente |
| Integrações | APIs, formatos, autenticação ou limites de utilização desconhecidos | Confirmar viabilidade e custos por fonte | Pendente |
| Operação | Custos de execução, suporte e manutenção desconhecidos | Estimar custo total e definir responsável operacional | Pendente |
| Governança | Distribuição upstream e adoção ainda não comprovadas ponta a ponta | Concluir validação documentada por PR e aprovação separada | Pendente |

## 7. Plano inicial proposto

1. **Confirmar mandato e partes interessadas:** registar patrocinador, aprovador autorizado, responsável e revisor independente.
2. **Validar problema e beneficiários:** recolher evidência do processo atual e selecionar utilizadores representativos.
3. **Fechar escopo e riscos:** aprovar inclusões, exclusões, dependências, dados e obrigações relevantes.
4. **Aprovar critérios de aceitação:** definir linha de base, amostra, métricas, metas, método e responsáveis.
5. **Concluir controlos de governança:** obter aprovação independente das decisões necessárias e executar/documentar o teste operacional de distribuição upstream por PR.
6. **Submeter decisão formal de G0:** anexar evidências e obter aprovação explícita conforme a autoridade aplicável.
7. **Só após aprovação:** atualizar o estado do Gate mediante PR revisada. Qualquer implementação funcional depende dessa decisão e de uma autorização de escopo subsequente, se exigida.

Prazos, orçamento, capacidade da equipa e datas do piloto permanecem **por definir**, pois não foram fornecidos dados suficientes para estimativas responsáveis.

## 8. Evidências obrigatórias para decisão de G0

- [ ] Problema específico validado e resultado esperado mensurável.
- [ ] Beneficiários, necessidades e utilizadores prioritários identificados com evidência.
- [ ] Patrocinador, aprovador autorizado e responsável formalmente confirmados.
- [ ] Escopo inicial e exclusões revistos e aceites.
- [ ] Riscos, dependências, dados e obrigações relevantes avaliados.
- [ ] Critérios de aceitação, linha de base e plano inicial aprovados.
- [ ] Revisor independente identificado; decisão formal registada por via verificável.
- [ ] Estado da adoção GOVERNANCA e evidência do teste de distribuição por PR atualizados separadamente.
- [ ] PR documental aprovada por pessoa elegível e integrada segundo as regras do repositório.

## 9. Estado de decisão e regra fail-closed

- **Estado do Gate G0:** BLOQUEADO / AGUARDANDO EVIDÊNCIA.
- **Estado desta proposta:** EM REVISÃO; NÃO APROVADA.
- **Aprovador e data de aprovação:** não registados.
- **Evidência de aprovação:** inexistente nesta proposta.
- **`LICITACAO.enabled`:** deve permanecer `false`.
- **Módulos funcionais:** não iniciar.
- **Adoção GOVERNANCA:** decisão separada, não aprovada por este documento.

Qualquer critério não demonstrado permanece pendente. Não atribuir pontos por intenção, por existência de documentação não validada ou por sucesso de CI que apenas verifica controlos técnicos. Não alterar o registo central nem declarar G0 aprovado até todas as condições aplicáveis estarem comprovadas e aprovadas formalmente.
