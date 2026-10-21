# Modelo operacional — vendedor governamental no Brasil

- **ID:** LIC-OPS-BR-001
- **Versão:** 1.0 — proposta de conceção
- **Estado:** DOCUMENTAÇÃO NÃO FUNCIONAL / PARA REVISÃO
- **Jurisdição:** Brasil
- **Perfil:** PME fornecedora
- **Categorias:** bens, serviços, tecnologia/software, consultoria, obras e engenharia
- **Automação:** assistida, com decisões críticas humanas
- **Gate G0:** BLOQUEADO — este documento não constitui aprovação
- **Issue de governação:** [LICITACAO #6](https://github.com/carlos-andrade/LICITACAO/issues/6)

> Este documento prepara a conceção do processo. Não autoriza desenvolvimento de módulos funcionais, não altera o registo central da GOVERNANCA e não muda `LICITACAO.enabled=false`.

## 1. Objetivo e resultados esperados

Definir um processo rastreável para uma PME que vende ao poder público brasileiro, da identificação da oportunidade até ao recebimento e encerramento do contrato.

Resultados operacionais propostos:
1. Oportunidades com fonte oficial, prazos e objeto rastreáveis.
2. Decisão bid/no-bid fundamentada antes de investir na proposta.
3. Requisitos do edital associados a evidências, responsáveis e estado.
4. Proposta técnica e financeira aprovada antes da submissão.
5. Contratos, entregas, faturação e pagamentos reconciliáveis.
6. Histórico auditável de decisões, documentos, aprovações e exceções.

Indicadores sugeridos para validação com os beneficiários: taxa de oportunidades qualificadas, taxa bid/no-bid, submissões dentro do prazo, taxa de habilitação, taxa de sucesso, margem prevista versus realizada, entregas aceites no prazo, prazo de recebimento e saldo vencido. Metas numéricas ficam pendentes de baseline e aprovação.

## 2. Escopo proposto

### Incluído
- Bens, serviços, tecnologia/software, consultoria, obras e engenharia.
- Fontes oficiais federais, estaduais, municipais e de estatais, conforme o regime aplicável.
- Captura e qualificação de oportunidades; análise documental; preparação e validação de propostas; submissão supervisionada; acompanhamento do julgamento; contratualização; execução; faturação, recebimento e encerramento.
- Gestão documental, tarefas, prazos, riscos, aprovações, indicadores e auditoria como capacidades transversais.
- Automação assistida: extração, classificação, alertas, cálculos e verificações preliminares com revisão humana.

### Excluído nesta proposta
- Submissão autónoma, assinatura autónoma, declarações legais automáticas ou compromissos financeiros automáticos.
- Alteração automática do registo de consumidores da GOVERNANCA ou ativação do projeto.
- Parecer jurídico automático que substitua profissional competente.
- Integrações produtivas, credenciais, robôs de portais ou módulos de negócio antes da aprovação formal de G0.
- Garantia de elegibilidade ou vitória em qualquer procedimento.

## 3. Fluxo de fases e gates

| Fase | Atividades e artefactos | Gate de saída | Condição mínima |
|---|---|---|---|
| G0 — governação do projeto | Problema, beneficiários, patrocinador, owner, escopo, riscos, critérios e plano | G0 | Aprovação formal verificável; atualmente BLOQUEADO |
| 1. Inteligência de mercado | Registo de oportunidade, fonte, órgão, objeto, datas e anexos | G1 — oportunidade | Fonte e procedimento identificáveis; prazos confirmados ou marcados pendentes |
| 2. Qualificação | Elegibilidade, capacidade, concorrência, viabilidade e risco | G2 — bid/no-bid | Decisão humana registada: BID, NO_BID ou PENDENTE |
| 3. Análise do procedimento | Edital, anexos, retificações, requisitos e dúvidas | G3 — conformidade | Requisitos críticos classificados; impedimentos e dúvidas materiais tratados |
| 4. Preparação da proposta | Solução técnica, memória de custos, preço, margem e documentos | G4 — proposta | Validações técnica e financeira e aprovação do preço |
| 5. Validação e submissão | Checklist, aprovação final, envio e recibo | G5 — submissão | Autorização humana e comprovativo da versão enviada |
| 6. Julgamento | Sessões, diligências, classificação, recursos e decisões | G6 — resultado | Resultado sustentado por evidência oficial e próximos prazos atribuídos |
| 7. Contratualização | Revisão de instrumento, obrigações, garantias e assinatura | G7 — contrato | Termos revistos e assinatura por representante autorizado |
| 8. Execução | Entregas, medições, aceite, ocorrências e alterações | G8 — execução | Evidências de execução/aceite e pendências registadas |
| 9. Faturação e encerramento | Faturas, liquidação, pagamentos, reconciliação e arquivo | G9 — fecho | Saldos e obrigações reconciliados; pendências fechadas ou transferidas formalmente |

Nenhum gate é aprovado pela mera conclusão aparente das tarefas. É obrigatório registar decisão, aprovador autorizado, data, fundamento e evidências.

## 4. Responsabilidades

Papéis a nomear formalmente após validação do contexto real. A tabela não nomeia pessoas nem constitui designação formal.

| Papel | Responsabilidade | Decisão/controlo |
|---|---|---|
| Patrocinador/direção | Prioridades, recursos e apetite ao risco | Aprova G0 e compromissos reservados à direção |
| Owner do projeto | Escopo, dependências, entregas e aceitação do projeto | Coordena plano e reporte; nomeação formal pendente |
| Comercial governamental | Funil, qualificação e estratégia | Recomenda bid/no-bid |
| Líder de licitação | Edital, calendário, matriz de conformidade e coordenação | Confirma completude do processo |
| Especialista técnico | Especificações, solução, capacidade e execução | Valida conformidade técnica |
| Financeiro | Custos, margem, caixa, faturação e reconciliação | Valida viabilidade e controlos financeiros |
| Jurídico/assessor competente | Regime, declarações, riscos e contrato | Emite revisão nos casos definidos |
| Gestor do contrato | Obrigações, entregas, ocorrências e fecho | Confirma evidência operacional |
| Administrador do sistema | Acessos, configurações e trilho técnico | Não substitui aprovação de negócio |

Segregação mínima: quem prepara preço ou proposta não deve ser a única pessoa a aprovar o seu próprio compromisso final quando exista outra pessoa autorizada disponível. Exceções de PME devem ser explicitamente aprovadas e registadas.

## 5. Documentos e evidências

| Família | Exemplos | Metadados/controlo |
|---|---|---|
| Oportunidade | Aviso, edital, anexos, URL e publicação | Fonte, data de captura, versão e hash |
| Habilitação | Atos constitutivos, poderes, certidões, declarações e registos aplicáveis | Emissor, validade, titular e acesso restrito |
| Técnica | Catálogos, fichas, atestados e certificações | Requisito relacionado e versão |
| Qualificação | Checklist, risco, capacidade e decisão bid/no-bid | Autor, aprovador, data e fundamento |
| Esclarecimentos | Perguntas, respostas, atas e retificações | Referência oficial e prazo |
| Proposta | Versões técnica/financeira, custos e aprovações | Versão aprovada e versão submetida imutável |
| Julgamento | Recibo, atas, diligências, classificação e recursos | Origem e estado oficial |
| Contrato | Instrumento, anexos, garantias e alterações | Vigência, signatários e versão válida |
| Execução | Ordens, entregas, medições, aceite e ocorrências | Obrigação, prazo e prova |
| Financeiro | Nota fiscal, protocolo, liquidação, pagamento e reconciliação | Contrato, entrega, valor e estado |

A política de retenção, privacidade e classificação documental depende de validação jurídica e operacional. Credenciais e segredos nunca devem ser armazenados como documentos comuns.

## 6. Modelo de dados lógico

Entidades propostas:
- `Fornecedor`: identificador interno, razão social, CNPJ, atividades e capacidade.
- `OrgaoContratante`: nome, esfera, unidade e portal.
- `Oportunidade`: fonte, URL, objeto, órgão, datas, valor estimado, categoria e estado.
- `Procedimento`: identificador oficial, regime jurídico, modalidade, critério, lotes e versão do edital.
- `Requisito`: fonte, tipo, obrigatoriedade, evidência, responsável, prazo e estado.
- `Documento`: tipo, versão, hash, origem, validade, classificação e entidade associada.
- `Decisao`: tipo, decisão, fundamento, autor, aprovador, data e evidências.
- `Proposta` e `ItemProposta`: versões, escopo, quantidade, custo, preço, unidade e especificação.
- `Contrato` e `ObrigacaoContratual`: instrumento, vigência, valor, prazo, aceite e responsável.
- `Entrega`: item, quantidade, data, protocolo, aceite e não conformidade.
- `Fatura` e `Pagamento`: valores, datas, estado e referências de reconciliação.
- `TarefaPrazo`: evento, prazo, responsável, escalonamento e estado.
- `AuditoriaEvento`: ator, ação, data/hora, entidade, resultado e referência.

Regras de integridade:
1. A versão submetida da proposta é imutável e recuperável.
2. Retificações geram nova versão e uma análise de impacto sobre requisitos.
3. Decisões de gate têm aprovador autorizado e evidências.
4. Preço aprovado, preço submetido, valor contratual, faturado e recebido são campos distintos.
5. Prazos guardam fonte e fuso horário; a data calculada não substitui validação oficial.
6. Alterações contratuais preservam o histórico e a referência ao instrumento autorizador.
7. Acesso segue menor privilégio; dados pessoais e segredos são protegidos.

## 7. Estados do processo

Estados propostos: `CAPTURADA`, `EM_QUALIFICACAO`, `PENDENTE_INFORMACAO`, `BID_APROVADO`, `NO_BID`, `EM_ANALISE`, `EM_PREPARACAO`, `AGUARDA_APROVACAO`, `APROVADA_PARA_ENVIO`, `SUBMETIDA`, `SUBMISSAO_COMPROVADA`, `EM_JULGAMENTO`, `RESULTADO_REGISTADO`, `EM_CONTRATUALIZACAO`, `EM_EXECUCAO`, `EM_FECHO`, `ENCERRADA`, `ENCERRADA_COM_PENDENCIAS`, `SUSPENSA`, `DESCLASSIFICADA_OU_INABILITADA`, `REVOGADA_OU_ANULADA`.

As transições são controladas por gates e evidências. `SUBMETIDA` não equivale a `SUBMISSAO_COMPROVADA`; resultado provisório não equivale a decisão final.

## 8. Automação assistida e limites

| Capacidade | Pode automatizar | Exige intervenção humana |
|---|---|---|
| Descoberta | Recolha de metadados, deduplicação e alertas | Confirmar fonte e relevância |
| Documentos | OCR, extração e classificação preliminar | Interpretar requisitos críticos |
| Prazos | Calendário e escalonamento | Validar prazo oficial e consequência |
| Qualificação | Pontuações e cenários | Aprovar bid/no-bid |
| Preço | Cálculos, sensibilidade e alertas | Aprovar preço final |
| Proposta | Modelos e verificações de consistência | Aprovar declarações e versão final |
| Submissão | Checklist e preparação | Autorizar envio e confirmar recibo |
| Contrato | Extração de obrigações e prazos | Aprovar termos e assinar |
| Execução | Alertas e conciliação preliminar | Confirmar aceite e alterações |
| Fecho | Previsões e reconciliação preliminar | Validar saldos e encerramento |

Falhas de integração devem gerar erro/pêndencia, nunca sucesso presumido. Nenhum agente pode submeter, assinar, declarar factos ou assumir compromisso financeiro sem autorização humana explícita.

## 9. Enquadramento jurídico de referência

O regime deve ser identificado em cada procedimento, sem assumir que todas as entidades seguem a mesma lei. Referências iniciais para validação:
- Lei nº 14.133/2021, quando aplicável.
- Lei Complementar nº 123/2006, quanto ao tratamento de ME/EPP, sujeito a enquadramento e condições legais.
- Lei nº 13.303/2016 para empresas públicas e sociedades de economia mista, quando aplicável.
- Regulamentos do ente, edital, normas setoriais e legislação complementar aplicável.

Fontes oficiais: [Planalto](https://www.planalto.gov.br/), [PNCP](https://www.gov.br/pncp/pt-br), [Compras.gov.br](https://www.gov.br/compras/pt-br). Este texto não é parecer jurídico; a aplicabilidade deve ser validada caso a caso.

## 10. Critérios de aceitação da conceção

| ID | Critério | Evidência requerida |
|---|---|---|
| AC-01 | Ciclo completo documentado | Fluxo das nove fases revisto |
| AC-02 | Cada fase possui gate, entradas, saídas e bloqueios | Matriz de gates aprovada |
| AC-03 | Bid/no-bid é decisão explícita | Casos BID, NO_BID e PENDENTE |
| AC-04 | Requisitos rastreiam a fonte e a evidência | Matriz de conformidade |
| AC-05 | Versão submetida é recuperável | Documento e recibo de submissão |
| AC-06 | Preço, contrato, fatura e pagamento reconciliáveis | Modelo e testes de integridade |
| AC-07 | Ações críticas exigem autorização humana | Matriz de permissões e testes negativos |
| AC-08 | Falhas, prazos e documentos expirados são detetados | Casos de teste registados |
| AC-09 | Decisões e alterações têm trilho de auditoria | Registos com ator, data e evidência |
| AC-10 | Regime jurídico é explícito por procedimento | Cenários revistos por pessoa competente |
| AC-11 | Fecho distingue recebido, pendente e em disputa | Testes de reconciliação |
| AC-12 | Acesso, retenção e privacidade estão definidos | Política validada |
| AC-13 | Exceções e estados terminais são tratados | Testes de suspensão, desistência e erro |
| AC-14 | Beneficiários validam o desenho | Ata e lista de alterações |

Cenários mínimos: fornecedor inelegível; certidão expirada; retificação do edital; submissão sem recibo; preço abaixo do limite interno; alteração contratual; fatura não paga; integração indisponível.

## 11. Riscos, dependências e questões abertas

- **Beneficiários e necessidades:** não formalmente identificados.
- **Patrocinador e owner:** não formalmente nomeados; a tabela de papéis é apenas uma proposta.
- **Baseline e metas:** não fornecidos; não inventar objetivos quantitativos.
- **Fontes e integrações:** confirmar portais prioritários, disponibilidade e termos de uso.
- **Jurídico:** validar regime, documentos, prazos, tratamento de ME/EPP e retenção.
- **Financeiro:** validar limites de margem, capital de giro, garantias e alçadas de aprovação.
- **Segurança:** definir identidade, acesso, segredos, logs e proteção de dados.
- **Governação upstream:** falta executar e documentar o teste real de distribuição por PR.

## 12. Gate G0 e decisão atual

**Estado: BLOQUEADO / AGUARDANDO EVIDÊNCIA.** Este documento responde apenas à elaboração de uma proposta de processo. Não prova necessidade validada, nomeação formal, aprovação de critérios ou aprovação do G0.

Para considerar G0:
1. Confirmar problema operacional e resultado verificável com evidência.
2. Identificar beneficiários e necessidades.
3. Nomear formalmente patrocinador e owner.
4. Aprovar escopo, exclusões, riscos e dependências.
5. Aprovar critérios de aceitação e plano inicial.
6. Registar aprovação explícita por autoridade competente.
7. Concluir a validação operacional de distribuição upstream e os controlos da GOVERNANCA antes de solicitar qualquer ativação.

A issue [LICITACAO #6](https://github.com/carlos-andrade/LICITACAO/issues/6) permanece aberta. A distribuição não pode ser declarada executada sem URLs de runs, artefactos e PR de sincronização verificáveis. `LICITACAO.enabled` deve permanecer `false`.
