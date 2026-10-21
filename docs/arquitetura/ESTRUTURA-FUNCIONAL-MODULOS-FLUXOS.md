# Estrutura funcional e fluxos de negócio — LICITACAO

- ID: LIC-FUNC-ARCH-001
- Versão: 0.1.0 — proposta documental
- Estado: PARA REVISÃO; NÃO APROVADO PARA IMPLEMENTAÇÃO
- Jurisdição: Brasil; perfil de referência: PME fornecedora ao setor público
- Gate G0: BLOQUEADO / AGUARDANDO EVIDÊNCIA
- LICITACAO.enabled: false

> Este documento descreve uma arquitetura funcional proposta. Não implementa software, não constitui parecer jurídico, não aprova G0 nem autoriza integrações produtivas, submissão autónoma, assinatura, lances ou compromissos financeiros.

## 1. Princípios

1. Rastrear oportunidade, fonte, decisão, requisito, documento, versão, submissão e obrigação até às respetivas evidências.
2. Exigir aprovação humana para bid/no-bid, preço, submissão, assinatura, recursos e exceções materiais.
3. Aplicar fail-closed: informação crítica ausente, vencida, contraditória ou não validada bloqueia a transição.
4. Guardar URL oficial, instante de captura, versão, retificações e hash dos documentos.
5. Separar estado externo do procedimento e estado interno; preço aprovado e submetido; contrato, faturação e recebimento.
6. Tratar automação como assistência sujeita a revisão, nunca como prova autónoma de conformidade.
7. Usar menor privilégio, segregação de funções, auditoria e proteção de dados.
8. Confirmar regime e prazos nas fontes aplicáveis; não inferir conclusões jurídicas apenas pela categoria comercial.

## 2. Mapa de módulos

| ID | Módulo | Responsabilidade | Saída |
|---|---|---|---|
| M00 | Governança e auditoria | Papéis, políticas, gates, permissões e histórico | Decisões e eventos auditáveis |
| M01 | Cadastro e capacidade | Perfil empresarial, categorias, documentos e validade | Perfil e lacunas de habilitação |
| M02 | Inteligência de oportunidades | Captura de fontes públicas e oportunidades | Oportunidade com fonte e datas |
| M03 | Qualificação / bid-no-bid | Aderência, capacidade, risco, prazo e economia | Decisão fundamentada |
| M04 | Análise do edital | Requisitos, anexos, retificações e evidências | Matriz de conformidade |
| M05 | Produtos, fornecedores e custos | Cotações, equivalência, disponibilidade, logística e custos | Custo total reproduzível |
| M06 | Proposta técnica e comercial | Solução, documentos, preço, margem e versões | Pacote candidato à aprovação |
| M07 | Aprovação e submissão assistida | Checklist, autorização, versão enviada e recibo | Prova de submissão |
| M08 | Julgamento e diligências | Eventos, notificações, classificação e recursos | Linha temporal e próximos passos |
| M09 | Contratos e obrigações | Instrumento, vigência, garantias e obrigações | Contrato e calendário |
| M10 | Execução, entrega e aceite | Entregas, medição, aceite e ocorrências | Evidência de execução |
| M11 | Faturação e recebimento | Faturas, liquidação, pagamentos e reconciliação | Saldos e divergências |
| M12 | Tarefas e notificações | Prazos, responsáveis, alertas e escalonamento | Tarefas e histórico |
| M13 | Relatórios e indicadores | Métricas operacionais e financeiras | Relatórios com origem e data de corte |

M00 e M12 são transversais. M13 é somente de leitura. A ordem é uma dependência lógica proposta, não autorização de implementação.

## 3. Fluxo principal

```text
Fonte oficial
 -> M02 Registar oportunidade
 -> M03 Decidir BID / NO_BID / PENDENTE
 -> M04 Analisar edital e requisitos
 -> M05 Validar produto, fornecedor, custo e viabilidade
 -> M06 Preparar proposta versionada
 -> M00 Aprovação humana do pacote final
 -> M07 Submissão assistida e registo do recibo
 -> M08 Acompanhar julgamento e diligências
 -> Não adjudicada: encerrar com motivo e evidência
 -> Adjudicada: M09 Rever contrato e obrigações
 -> M10 Executar, entregar e obter aceite
 -> M11 Faturar, acompanhar liquidação e reconciliar
 -> M13 Relatórios e encerramento auditável
```

Qualquer fase pode terminar em BLOQUEADO, PENDENTE ou ENCERRADO SEM AVANÇO. Retificações materiais reabrem a análise de impacto e podem invalidar aprovações anteriores.

## 4. Contrato funcional por módulo

### M00 — Governança e auditoria
- Entradas: identidade, permissões, políticas aprovadas e pedidos de decisão.
- Processamento: validar autorização, segregação e pré-condições; registar ator, data/hora, fundamento e evidência.
- Saídas: decisão de permitir/bloquear e evento de auditoria.
- Bloqueios: papel não autorizado, gate pendente ou política ausente.
- Aceitação: ações críticas sem permissão são recusadas; correções não apagam histórico.
- Dependências: todos os módulos.

### M01 — Cadastro e capacidade
- Entradas: dados da empresa, categorias, capacidade e documentos.
- Processamento: verificar completude, titularidade e validade.
- Saídas: perfil, capacidades e documentos em falta/vencidos.
- Bloqueios: identificador inconsistente ou documento vencido.
- Aceitação: alegações de habilitação apontam para documento, emissor, validade e data de verificação; não se declara elegibilidade jurídica definitiva.
- Dependências: M00, M12.

### M02 — Inteligência de oportunidades
- Entradas: fonte oficial, URL, aviso, edital e anexos.
- Processamento: registar origem, deduplicar com revisão e extrair preliminarmente objeto, órgão, lotes e datas.
- Saídas: oportunidade e versões documentais.
- Bloqueios: fonte não verificável, anexo ausente, data ambígua ou conflito com retificação.
- Aceitação: URL, instante de captura e estado de confirmação dos prazos sempre presentes.
- Dependências: M00, M12.

### M03 — Qualificação e bid/no-bid
- Entradas: oportunidade, perfil, requisitos preliminares, capacidade, risco e estimativa económica.
- Processamento: avaliar aderência, impedimentos, prazo, esforço, capital e margem.
- Saídas: recomendação e decisão humana BID, NO_BID ou PENDENTE, com fundamento/aprovador.
- Bloqueios: impedimento desconhecido, capacidade insuficiente ou custo não validado.
- Aceitação: não avançar sem decisão registada; NO_BID exige motivo.
- Dependências: M01, M02, M05 preliminar, M00.

### M04 — Análise do edital
- Entradas: edital, anexos, retificações, respostas oficiais e decisão BID.
- Processamento: decompor requisitos administrativos, técnicos, comerciais, entrega e pagamento; associar evidência, responsável e prazo.
- Saídas: matriz CONFORME, NÃO_CONFORME, PENDENTE, NÃO_APLICÁVEL (com fundamento) ou EM_REVISÃO.
- Bloqueios: requisito crítico sem evidência, retificação não analisada ou prazo não confirmado.
- Aceitação: requisito remete para cláusula/fonte; extração automática não fecha requisito crítico.
- Dependências: M01, M02, M03, M00, M12.

### M05 — Produtos, fornecedores e custos
- Entradas: especificações, catálogo, cotações, disponibilidade, frete, seguros, tributos e condições de pagamento.
- Processamento: comparar equivalência, validade, custo posto no destino, abastecimento e necessidade de caixa.
- Saídas: mapa de fornecimento e memória de custo por item/lote.
- Bloqueios: equivalência não demonstrada, cotação vencida ou custo relevante omitido.
- Aceitação: cálculo reproduzível e premissas explícitas; estimativa separada de cotação confirmada.
- Dependências: M01, M02, M04, M00.

### M06 — Proposta técnica e comercial
- Entradas: matriz de conformidade, solução, documentos, custos e condições.
- Processamento: preparar itens/lotes, anexos, preço/margem segundo regras aprovadas e versões.
- Saídas: pacote candidato à aprovação.
- Bloqueios: requisito crítico pendente, documento vencido, custo não validado ou divergência técnica.
- Aceitação: versão identificada por hash; alteração posterior invalida aprovação anterior.
- Dependências: M04, M05, M01, M00.

### M07 — Aprovação e submissão assistida
- Entradas: pacote final, decisão BID e aprovações.
- Processamento: checklist, autorização humana, registo do operador, versão enviada e recibo.
- Saídas: comprovativo, instante e versão submetida.
- Bloqueios: autorização ausente, prazo incerto ou divergência de versão.
- Aceitação: não declarar submissão concluída sem recibo ou evidência alternativa formalmente aceite; sem submissão autónoma nesta proposta.
- Dependências: M00, M04, M06, M12.

### M08 — Julgamento e diligências
- Entradas: recibo, publicações, atas e notificações.
- Processamento: linha temporal, prazos e confronto entre estado interno e oficial.
- Saídas: estado fundamentado e diligências atribuídas.
- Bloqueios: notificação sem fonte, prazo não confirmado ou recurso sem revisão competente.
- Aceitação: evento material tem origem/data; respostas e recursos exigem aprovação antes do envio.
- Dependências: M07, M00, M12.

### M09 — Contratos e obrigações
- Entradas: resultado oficial, contrato, anexos, proposta vencedora, garantias e poderes.
- Processamento: comparar proposta/contrato; identificar obrigações, marcos, vigência, penalidades e pagamentos.
- Saídas: contrato revisto e calendário de obrigações.
- Bloqueios: divergência material, poderes não confirmados ou obrigação sem responsável.
- Aceitação: assinatura é humana; obrigação tem fonte, responsável, prazo e prova esperada.
- Dependências: M08, M00, M12.

### M10 — Execução, entrega e aceite
- Entradas: contrato, ordens, plano de entrega, itens e prazos.
- Processamento: acompanhar expedição, entrega, medição, aceite e ocorrências.
- Saídas: protocolo, evidência de execução e aceite/rejeição.
- Bloqueios: alteração sem autorização, quantidade divergente ou prova ausente.
- Aceitação: obrigação só é concluída após evidência adequada validada.
- Dependências: M09, M05 quando aplicável, M00, M12.

### M11 — Faturação e recebimento
- Entradas: contrato, aceite, documento fiscal, protocolo e pagamento.
- Processamento: ligar fatura à obrigação, acompanhar vencimentos e reconciliar valores.
- Saídas: contas a receber, divergências e saldo.
- Bloqueios: falta de aceite, referência inconsistente ou valor divergente.
- Aceitação: contratado, faturado, liquidado e recebido são valores distintos; ajuste tem autor, motivo e evidência.
- Dependências: M09, M10, M00, M12.

### M12 — Tarefas e notificações
- Entradas: prazos confirmados, obrigações e regras aprovadas.
- Processamento: agendar, atribuir, alertar, escalonar e registar confirmação.
- Saídas: fila de tarefas e histórico.
- Bloqueios: prazo sem fonte/regra confirmada ou destinatário inexistente.
- Aceitação: alerta não substitui fonte oficial; origem e fuso horário ficam registados.
- Dependências: transversal.

### M13 — Relatórios e indicadores
- Entradas: dados operacionais, definições de métricas e data de corte.
- Processamento: calcular indicadores com período, denominador, origem e tratamento de ausências.
- Saídas: funil, conversão, conformidade, submissões no prazo, resultados, margem, execução e recebíveis.
- Bloqueios: dados insuficientes ou métrica ambígua.
- Aceitação: ausência de registo não equivale a zero; separar confirmado, estimado e ausente.
- Dependências: leitura dos módulos, sem alterar registos.

## 5. Fluxos de exceção

1. Retificação: guardar nova versão → identificar requisitos afetados → suspender aprovações potencialmente inválidas → rever impacto/prazos → nova aprovação humana.
2. Documento vencido: marcar não utilizável → identificar processos afetados → renovar → revalidar.
3. Falha de cotação: bloquear cálculo → buscar alternativa comparável → recalcular → rever margem e aprovação.
4. Prazo incerto: consultar fonte oficial e manter bloqueado até confirmação.
5. Falha do portal: registar hora/evidência → aplicar apenas contingência oficial validada → não declarar submissão sem prova.
6. Diligência/recurso: preservar notificação → confirmar prazo → revisão competente → aprovação e prova de envio.
7. Entrega atrasada/recusada: abrir ocorrência → avaliar obrigação/impacto → decisão autorizada antes de alteração.
8. Divergência financeira: saldo não reconciliado → associar evidências → corrigir por evento auditável.
9. Incidente de acesso/dados: restringir acesso segundo plano aprovado, preservar logs e escalar.
10. Falha de automação: marcar não verificado e encaminhar para revisão manual; nunca inferir sucesso.

## 6. Estados e transições

Estados comuns propostos: RASCUNHO, EM_ANALISE, PENDENTE_EVIDENCIA, AGUARDANDO_APROVACAO, APROVADO, BLOQUEADO, REJEITADO, CONCLUIDO, CANCELADO e ENCERRADO. Cada entidade define subconjunto e transições permitidas.

- Só papel autorizado executa aprovações.
- Transição crítica regista ator, instante, fundamento e evidências.
- BLOQUEADO não pode ser contornado por automação.
- CONCLUIDO exige critérios de saída satisfeitos.
- Reabertura cria evento e motivo; não apaga histórico.
- Estado externo conserva fonte e instante de consulta.

## 7. Entidades e relações

- Fornecedor 1:N Documento, Capacidade e Cotação.
- Oportunidade 1:N Evento de fonte, Decisão e Tarefa; relaciona-se com Procedimento/Lote.
- Procedimento/Lote 1:N Requisito, Versão de edital e Proposta.
- Requisito N:N Documento/Evidência, com responsável e estado.
- Proposta 1:N Versão, Item, Memória de cálculo e Aprovação.
- Proposta vencedora pode originar Contrato, preservando procedimento e versão adjudicada.
- Contrato 1:N Obrigação, Entrega, Fatura, Ocorrência e Alteração contratual.
- Entrega/aceite pode suportar Fatura; Fatura 1:N Evento de pagamento/ajuste.
- Entidades relevantes referenciam AuditoriaEvento e evidências aplicáveis.

Identificadores oficiais e internos são distintos. Dados pessoais/comerciais devem ser minimizados e protegidos segundo política a aprovar.

## 8. Critérios transversais de aceitação

- Nenhum gate é aprovado implicitamente pela ausência de erro.
- Não submeter sem versão final aprovada e autorização humana.
- A versão submetida é recuperável e imutável.
- Datas, moeda, unidades e cálculos têm regras explícitas.
- Fontes oficiais e retificações são rastreáveis.
- Acesso e alterações críticas são auditáveis.
- Falhas de integração/extração são visíveis e não se convertem em sucesso.
- Indicadores são recalculáveis a partir da origem.
- Testes futuros cobrem dados ausentes/duplicados, retificações, permissões insuficientes e recuperação de falhas.
- Validação jurídica, fiscal, de segurança, privacidade e operação requer responsáveis competentes.

## 9. Próximas fases documentais

1. Validar problema, beneficiários, patrocinador, owner e resultado mensurável para G0.
2. Rever módulos, escopo, exclusões e prioridades.
3. Nomear responsáveis e aprovadores por fluxo.
4. Validar requisitos legais/operacionais por tipo de procedimento.
5. Definir dados, permissões, retenção, auditoria e aceitação.
6. Elaborar especificações e testes antes de implementação.
7. Documentar aprovação formal de G0 e evidências de governança/distribuição aplicáveis.
8. Só depois submeter proposta separada de implementação para revisão/autorização.

## 10. Decisão atual

**DOCUMENTAÇÃO PROPOSTA; NÃO APROVADA PARA IMPLEMENTAÇÃO.** G0 permanece BLOQUEADO / AGUARDANDO EVIDÊNCIA. LICITACAO.enabled=false permanece obrigatório. Este documento não cria módulos de negócio nem autoriza workflows, integração produtiva ou alteração do registo central da GOVERNANCA.

Questões pendentes: beneficiário real; categorias prioritárias; tipos de procedimento prioritários; papéis disponíveis; limites de aprovação de preço/margem; portais a integrar; requisitos de segurança e retenção; metas e baseline.
