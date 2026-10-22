# Sistema LICITAÇÃO — Arquitetura Central
Versão: 0.1
Data: 22/10/2026
Repositório oficial: https://github.com/carlos-andrade/LICITACAO

## 1. Objetivo
Transformar os scripts, análises e documentos existentes em um sistema rastreável de apoio à identificação, análise, decisão, participação e execução de oportunidades de contratação pública.

## 2. Princípios arquiteturais
1. GitHub é a fonte versionada do código, das especificações e dos modelos documentais do projeto.
2. Cada oportunidade tem um identificador interno estável e conserva o identificador externo do PNCP ou do portal de origem.
3. Dados extraídos automaticamente devem manter origem, data/hora da captura, método, estado de validação e referência ao documento original.
4. Nunca tratar extração automática como verdade confirmada sem validação quando o dado afetar preço, habilitação, conformidade, prazo ou obrigação contratual.
5. Separar fatos do edital, dados fornecidos pelo usuário, dados de fornecedores, estimativas e decisões humanas.
6. O sistema recomenda e alerta; não envia proposta, dá lance, assume compromisso ou realiza ação irreversível sem autorização explícita.
7. Toda oportunidade deve ter cálculo de viabilidade com custos, margem, cenários e incertezas.
8. Credenciais, tokens e dados pessoais sensíveis não devem ser versionados no repositório.

## 3. Fluxo de ponta a ponta
1. Captura: localizar edital e registrar URL, órgão, modalidade, identificadores, datas e estado de captura.
2. Ingestão documental: obter aviso, termo de referência, anexos, retificações e documentos associados; registrar hash, nome, data e origem quando possível.
3. Normalização: criar registros consistentes de órgão, oportunidade, item, unidade, quantidade, valor de referência, local e prazo.
4. Análise de requisitos: extrair especificações, amostras, certificações, habilitação, atestados, entrega, pagamento, sanções e critérios de julgamento.
5. Validação: marcar cada requisito como confirmado, pendente, conflitante ou não aplicável; gerar lista de esclarecimentos.
6. Fornecedores: registrar contatos, produtos cotados, validade da cotação, estoque, prazo, frete, documentos técnicos e histórico de desempenho.
7. Motor econômico: calcular receita prevista, custo de aquisição, tributos, frete, logística, custos financeiros, contingência, lucro e margens.
8. Decisão: recomendar participar, investigar mais ou não participar, com motivos e condições explícitas.
9. Preparação e disputa: checklist de habilitação e proposta, calendário de prazos, preço-limite e registro autorizado das ações.
10. Resultado e contratação: registrar classificação, adjudicação/homologação, ata, contrato ou empenho.
11. Execução: acompanhar fornecimento, entrega, aceite, nota fiscal, liquidação, pagamento e ocorrências.
12. Aprendizado: comparar custos previstos e reais, registrar desempenho de fornecedor e atualizar premissas.

## 4. Modelo de dados lógico inicial
### Oportunidade
- id interno
- fonte e identificador externo
- URL de origem
- órgão/unidade compradora e UASG, quando houver
- modalidade, fundamento legal e critério de julgamento
- objeto
- datas de publicação, propostas, sessão, entrega e validade
- estado do processo
- valor estimado e moeda
- responsável interno
- data da última captura e estado da validação

### Documento
- id, oportunidade_id
- tipo documental
- nome, URL/origem, versão/data
- hash do conteúdo, quando calculável
- data de captura
- estado: capturado, falhou, pendente de revisão, validado
- observações e referência ao arquivo arquivado

### Item
- id, oportunidade_id e identificador no edital
- descrição original e descrição normalizada
- CATMAT/CATSER ou código externo, quando existente
- unidade, quantidade e valor unitário/total de referência
- especificações e requisitos técnicos
- local/prazo de entrega
- estado de validação e divergências

### Requisito
- id, item_id ou oportunidade_id
- categoria: técnico, habilitação, fiscal, entrega, prazo, pagamento ou outro
- texto original e interpretação
- fonte documental e página/seção
- estado: confirmado, pendente, conflitante, não aplicável
- evidência necessária e responsável pela validação

### Fornecedor e cotação
- fornecedor_id, razão social/nome, CNPJ quando necessário, contatos e origem do dado
- item/produto cotado e fabricante
- preço, unidade, quantidade mínima e disponibilidade
- frete, tributos informados, validade e prazo
- documentos técnicos e evidências de conformidade
- status da cotação e data de atualização

### Cenário econômico
- oportunidade_id/item_id
- preço de venda/lance planejado
- custo do produto
- impostos e premissas fiscais
- frete, entrega múltipla e manuseio
- custos administrativos/financeiros
- contingência
- custo total, lucro estimado, margem sobre receita e markup sobre custo
- preço máximo de compra e lance mínimo aceitável
- premissas, fontes, data e nível de confiança

### Decisão e evento
- decisão: participar, investigar, não participar
- justificativa, riscos, condições e aprovador
- eventos datados: mudança de prazo, esclarecimento, lance autorizado, resultado, empenho, entrega, aceite, faturamento, pagamento
- evidência associada e trilha de auditoria

## 5. Estados sugeridos para a oportunidade
CAPTURADA → DOCUMENTOS_PENDENTES → EM_ANALISE → AGUARDANDO_COTACOES → VIABILIDADE_CALCULADA → DECISAO_PENDENTE → APROVADA_PARA_PARTICIPAR → PROPOSTA_PREPARADA → EM_DISPUTA → RESULTADO_PUBLICADO → CONTRATADA/EMPENHADA → EM_EXECUCAO → ENTREGUE → FATURADA → PAGA → ENCERRADA.

Estados alternativos: DESCARTADA, INVIAVEL, SUSPENSA, REVOGADA, FRACASSADA, DESERTA. Toda transição deve registrar data, motivo e ator. Não avançar automaticamente quando faltar validação crítica.

## 6. Regras do motor econômico
- Receita estimada = quantidade vendida × preço unitário efetivo.
- Custo total = aquisição + tributos incrementais atribuíveis + frete + entrega local + manuseio + custos financeiros + demais custos + contingência.
- Lucro estimado = receita − custo total.
- Margem sobre receita = lucro ÷ receita.
- Markup sobre custo = lucro ÷ custo total.
- Preço máximo de compra por unidade = (receita prevista − lucro-alvo em moeda − custos não relacionados à aquisição) ÷ quantidade.
- Exibir margem e markup separadamente; não confundir “lucro de 50% da receita” com “acréscimo de 50% sobre o custo”.
- Impostos devem usar o regime e a situação do fornecedor confirmados por fonte competente; estimativas devem ser claramente rotuladas.
- Permitir cenários conservador, base e otimista; não esconder custos desconhecidos, e sim listá-los como pendências.
- Preço de referência do edital não é necessariamente preço final de venda ou receita garantida.

## 7. Requisitos não funcionais
- Idempotência na captura: repetir uma coleta não deve criar duplicatas.
- Observabilidade: logs, códigos de erro, contagem de documentos encontrados e falhas.
- Resiliência: falha de um endpoint não deve apagar evidências já capturadas.
- Rastreabilidade: cada conclusão material deve apontar para fonte e data.
- Segurança: segredos em variáveis de ambiente/secret manager, nunca em arquivos versionados.
- Testabilidade: fixtures de páginas/API, testes de normalização e testes de cálculo com valores conhecidos.
- Portabilidade: separar regras de negócio dos conectores de portais e da interface.
- Revisão humana para requisitos técnicos, fiscais, habilitação e compromissos financeiros.

## 8. Arquitetura de componentes proposta
- Conectores de fontes públicas (PNCP e portais complementares).
- Camada de captura e arquivo documental.
- Serviço de normalização e validação.
- Catálogo de oportunidades, itens e requisitos.
- Cadastro de fornecedores e gestão de cotações.
- Motor de custo, margem e preço-limite.
- Workflow de decisões, prazos e eventos.
- Relatórios e painel operacional.
- Auditoria, logs e monitoramento.
- Adaptadores de exportação/importação para planilhas e documentos.

A tecnologia de banco de dados, API e interface deve ser escolhida após inspeção do código existente e um MVP delimitado; evitar introduzir uma stack nova antes desse inventário.

## 9. MVP recomendado
Entrega 1 — Inventário e contrato de dados:
- revisar scripts e documentos existentes;
- definir schemas versionados para oportunidade, item, documento, cotação e cenário econômico;
- importar um edital conhecido como caso de teste;
- validar cálculos e estados com testes automatizados.

Entrega 2 — Fluxo vertical de uma oportunidade:
- capturar uma oportunidade PNCP;
- registrar documentos e itens;
- revisar requisitos;
- incluir cotação e frete;
- gerar relatório de viabilidade;
- registrar decisão e prazos.

Entrega 3 — Painel e operação:
- listar oportunidades por estado e prazo;
- alertar dados ausentes e riscos;
- manter histórico e exportar relatório;
- validar captura repetida, logs e falhas.

## 10. Caso de referência inicial
Usar a Dispensa UFRJ nº 25/2026 como caso de teste funcional, sem pressupor que a oportunidade seja economicamente viável:
- receita de referência: R$ 6.199,05;
- quantidade: 715 pacotes;
- requisitos técnicos com divergência documental a validar;
- origem logística informada pelo usuário: CEP 05685-000;
- destinos: cinco pontos da UFRJ no Rio de Janeiro;
- meta econômica do usuário: lucro mínimo de 50% da receita de referência;
- imposto e frete ainda precisam de validação/cotação formal;
- nenhum preço de fornecedor deve ser marcado como confirmado sem proposta válida e prova de conformidade.

## 11. Critérios de aceite da fundação
- Documentos da arquitetura e schemas versionados no GitHub.
- Campos obrigatórios, enums e relações documentados.
- Exemplo UFRJ representado sem inventar dados pendentes.
- Fórmulas econômicas verificadas por testes.
- Separação clara entre valor confirmado, estimativa e dado ausente.
- Próxima etapa definida com tarefas pequenas e verificáveis.

## 12. Pendências e decisões em aberto
- Inspecionar a estrutura atual do repositório e evitar duplicar scripts ou modelos.
- Definir formato inicial dos schemas (JSON Schema recomendado para validação e intercâmbio).
- Definir persistência operacional após comparar requisitos: SQLite para MVP local ou PostgreSQL para uso multiusuário.
- Definir interface somente depois do fluxo vertical e modelo de dados.
- Confirmar o modelo de execução, ambiente e responsáveis por credenciais.
- Confirmar os limites legais/fiscais e os procedimentos autorizados antes de automatizar qualquer envio ou lance.
