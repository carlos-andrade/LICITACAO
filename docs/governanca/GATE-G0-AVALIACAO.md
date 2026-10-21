# Avaliação do Gate G0 — Entrada do projeto LICITACAO

| Campo | Valor |
|---|---|
| **ID** | LIC-G0-001 |
| **Projeto** | LICITACAO |
| **Gate** | G0 — Entrada |
| **Estado** | APROVADO — G0 e adoção documental aprovados com limitações |
| **Data da avaliação** | 2026-10-21 |
| **Autoridade normativa** | [Constituição da GOVERNANCA, secção 5](https://github.com/carlos-andrade/GOVERNANCA/blob/main/CONSTITUICAO.md) |
| **Inspeção associada** | [INSPECAO-DE-ADOCAO.md](INSPECAO-DE-ADOCAO.md) |
| **Decisão registada** | Pedido explícito do titular do repositório para resolver G0 e ativar LICITACAO, recebido em 2026-10-21; ver esta avaliação e o pedido de ativação pendente das condições técnicas de adoção |
| **Patrocinador / proprietário** | Carlos Andrade, conforme campo `owner` do registo-mestre da GOVERNANCA |
| **Responsável do projeto** | Carlos Andrade, conforme registo-mestre; responsabilidades funcionais especializadas serão atribuídas antes das respetivas operações |

## 1. Problema e resultado esperado

**Problema:** a avaliação manual de oportunidades de fornecimento a órgãos públicos brasileiros exige consultar avisos, editais, anexos, fornecedores e preços em fontes distintas. Lacunas de informação, requisitos técnicos não confirmados e custos incompletos podem levar a decisões comerciais inadequadas ou comprometer capital de giro.

**Resultado esperado:** estabelecer uma plataforma governada para identificar, analisar e acompanhar oportunidades de fornecimento de produtos a órgãos públicos brasileiros, com decisões comerciais rastreáveis, custos completos, conferência dos instrumentos convocatórios e preservação de capital. Este propósito está alinhado com o [README do projeto](../../README.md) e com a [Constituição local](../../CONSTITUICAO.md).

**Indicadores iniciais de aceitação:**
- 100% das oportunidades recomendadas para decisão têm ligação ao registo oficial do PNCP e aos documentos oficiais consultados, quando disponíveis.
- Campos obrigatórios ausentes, fontes indisponíveis e requisitos ambíguos ficam marcados como pendentes/UNKNOWN; nunca são presumidos como conformes.
- 100% das recomendações de participação incluem custo total, capital comprometido, prazo/logística e riscos conhecidos antes da decisão humana.
- 100% das decisões finais de participação, preço, habilitação, assinatura e execução contratual permanecem sob revisão humana autorizada.

Os indicadores são critérios-alvo para desenho e validação; não afirmam que a aplicação já está implementada ou que esses resultados já foram medidos.

## 2. Beneficiários e partes interessadas

- **Beneficiários diretos:** equipa comercial que pesquisa oportunidades e fornecedores; responsáveis financeiros que avaliam custo total, margem e capital de giro; responsáveis por habilitação/conformidade; responsáveis técnicos e logísticos que verificam especificações, disponibilidade, entrega e garantia.
- **Beneficiário institucional final da contratação:** órgão público comprador, na medida em que a proposta deve cumprir os requisitos do instrumento convocatório e as condições contratuais.
- **Patrocinador e responsável pelo projeto:** Carlos Andrade, proprietário identificado no registo-mestre e titular do pedido explícito de regularização.
- **Revisão especializada:** apoio jurídico, fiscal ou técnico deverá ser acionado quando a obrigação ou o risco exceder a competência da equipa; a plataforma não substitui esse aconselhamento.

## 3. Escopo inicial e exclusões

**Incluído na fase inicial:**
1. Descoberta e registo de oportunidades do Portal Nacional de Contratações Públicas (PNCP), tratado como fonte oficial primária.
2. Preservação de URLs, datas de consulta e referências aos avisos, editais, termos de referência e anexos.
3. Extração estruturada dos itens, quantidades, requisitos técnicos, prazos e condições de entrega, com estado de validação explícito.
4. Pesquisa de fornecedores e referências públicas de preço, identificando claramente fontes secundárias e exigindo confirmação.
5. Comparação preliminar de custo total, capital comprometido, riscos e critérios de participação/não participação.
6. Trilho de auditoria e revisão humana das recomendações.

**Excluído da fase inicial:**
- submissão automática de propostas ou lances;
- decisão autónoma de participação ou definição de preço final;
- assinatura ou aceitação automática de contratos;
- declaração automática de conformidade jurídica/fiscal;
- tratar informação secundária como confirmação oficial;
- guardar credenciais, segredos ou dados pessoais/comerciais desnecessários no Git.

## 4. Riscos iniciais e mitigação

| Risco | Mitigação obrigatória |
|---|---|
| PNCP ou anexos indisponíveis/incompletos | Registar a limitação, procurar a plataforma oficial indicada no instrumento e bloquear a decisão até obter evidência suficiente |
| Fonte secundária desatualizada ou incorreta | Identificar como secundária e confirmar dados relevantes na fonte oficial |
| Requisito técnico ou habilitação interpretado incorretamente | Ligar cada conclusão ao documento oficial e exigir revisão humana/especializada |
| Custo, imposto, frete, prazo ou capital de giro incompleto | Não recomendar participação sem modelo de custo total e validação financeira |
| Dados pessoais, segredos ou informação comercial expostos | Minimização, controlo de acesso e proibição de armazenar segredos no repositório |
| Decisão automatizada indevida | Manter decisão final e submissão sob controlo humano autorizado |

Este é um levantamento inicial para entrada do projeto; não equivale a parecer jurídico nem a certificação de conformidade.

## 5. Critérios de aceitação e plano inicial

| ID | Critério de aceitação | Evidência / estado |
|---|---|---|
| AC-01 | Propósito, problema e indicadores iniciais definidos | Esta avaliação e README; documentado |
| AC-02 | Beneficiários e papéis de patrocínio/responsabilidade identificados | Esta avaliação e registo-mestre; documentado |
| AC-03 | Escopo e exclusões delimitados | Secção 3; documentado |
| AC-04 | Riscos e mitigações iniciais registados | Secção 4; documentado |
| AC-05 | Critérios objetivos e plano inicial definidos | Esta secção; definido para validação nas fases seguintes |
| AC-06 | Adoção individual da GOVERNANCA e distribuição upstream validadas | CONCLUÍDO COM LIMITAÇÕES: PR #24 integrada; 79/79 SHA iguais; CI pós-merge PASS; checklist WATCHDOG executada com 7 UNKNOWN |
| AC-07 | Autorização de ativação registada no repositório-mestre | CONCLUÍDO: GOVERNANCA PR #32 integrada; `LICITACAO.enabled=true` efetivo para âmbito de distribuição |

**Plano inicial:** (1) distribuição documental concluída por PR #24; (2) checklist WATCHDOG executada, com sete controlos UNKNOWN explícitos; (3) CI pós-merge e integridade de 79/79 espelhos confirmadas; (4) adoção documental aprovada com limitações; (5) integrar a GOVERNANCA PR #32 pelo processo autorizado para efetivar `enabled: true`.

## 6. Decisão G0

**Decisão: APROVADO para entrada e planeamento do projeto**, com base no propósito, beneficiários, papéis, escopo, exclusões, riscos e critérios iniciais documentados acima e na instrução explícita de regularização e ativação emitida pelo titular do repositório em 2026-10-21.

A distribuição upstream foi integrada pela [PR #24](https://github.com/carlos-andrade/LICITACAO/pull/24), com 79/79 Git blob SHA coincidentes e CI pós-merge PASS. A adoção documental fica aprovada com limitações; sete controlos WATCHDOG permanecem UNKNOWN e o WATCHDOG não é operacional. A alteração do registo-mestre para `enabled: true` foi integrada pela [GOVERNANCA PR #32](https://github.com/carlos-andrade/GOVERNANCA/pull/32), commit `cedba71292a107b1f4b5733987c6262d50c46673`.

- **Aprovador / patrocinador registado:** Carlos Andrade (titular indicado no registo-mestre).
- **Data da decisão:** 2026-10-21.
- **Evidência:** pedido explícito de resolução do Gate G0 e ativação, mais esta decisão versionada no repositório.
- **Estado de ativação no registo-mestre:** `true` desde a integração da [GOVERNANCA PR #32](https://github.com/carlos-andrade/GOVERNANCA/pull/32); âmbito de distribuição apenas.

## 7. Histórico

- 2026-10-21 — Reavaliação documental; problema, resultado, beneficiários, papéis, escopo, riscos e critérios iniciais consolidados. G0 aprovado; adoção documental aprovada com limitações após validação da distribuição; ativação central pendente de PR #32.

- 2026-10-21 — Estado de ativação reconciliado após a integração da GOVERNANCA PR #32; `enabled=true` efetivo para âmbito de distribuição.
