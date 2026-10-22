# Auditoria técnica inicial — LICITACAO

| Campo | Valor |
|---|---|
| ID | LIC-AUDIT-REPO-001 |
| Data da auditoria | 2026-10-22 |
| Repositório | [carlos-andrade/LICITACAO](https://github.com/carlos-andrade/LICITACAO) |
| Branch examinada | main |
| Commit examinado | cbed64fda61edc2e5e4309b5f055c9e3de80d76b |
| Tipo | Auditoria estática do conteúdo do repositório |
| Limitação | Não equivale a executar os scripts localmente nem a validar acesso atual à API PNCP |

## 1. Resumo executivo

A inspeção da árvore recursiva encontrou 192 caminhos no commit examinado, incluindo uma cópia espelhada de governança em `.governanca/upstream/` (112 caminhos). Fora desse espelho, há documentação de arquitetura, schemas JSON, exemplos, scripts Python para captura PNCP e cálculo de viabilidade, testes unitários da calculadora e workflows GitHub Actions.

**Conclusão:** o repositório já contém mais que documentação. Existem protótipos executáveis e uma primeira base de modelação. Ainda não há evidência suficiente para declarar a aplicação de negócio integrada, a captura PNCP completa em produção, os testes executados no ambiente atual ou um painel comercial implementado.

## 2. Inventário por tópico de evolução

| Tópico | Evidência encontrada | Estado auditado | Lacuna principal |
|---|---|---|---|
| Base documental | `README.md`, `EDITAIS/`, `COTAÇÃO/`, `COTAÇÕES APROVADAS/`, `FORNECEDORES/`, `ORÇAMENTOS/`, `docs/`, relatório PMESP em `docs/precificacao/` | PARCIAL | Validar conteúdo e completude de cada diretório; definir classificação, indexação, política de dados sensíveis e ligação entre evidências |
| Modelo de dados | `ARQUITETURA/schemas/` com schemas de oportunidade, item, cotação, decisão, documento e cenário económico; exemplos UFRJ | ESQUEMAS PRESENTES | Confirmar consistência entre schemas, relações, migrações e persistência; falta evidência de base de dados/aplicação integrada |
| Motor de decisão | `scripts/calculadora_viabilidade.py`, testes em `scripts/tests/test_calculadora_viabilidade.py`, schema de cenário económico e decisão | PROTÓTIPO PRESENTE | Executar testes; rever regras e arredondamentos; validar fiscalidade, custo completo e integração com decisão/habilitação |
| Captura PNCP | `scripts/pncp_capture.py`, `scripts/pncp_capture_integral.py`, respetivos READMEs | IMPLEMENTAÇÃO INICIAL PRESENTE | Testar endpoints e paginação reais, deduplicação, retries, limites, parsing de anexos/OCR, publicação segura e completude |
| Painel operacional | `assets/status-dashboard.svg` e visualização de status de governança | DASHBOARD COMERCIAL NÃO ENCONTRADO | Não foi encontrada aplicação web ou dashboard comercial com oportunidades, cotações, margens, prazos e decisões |

## 3. Componentes identificados

### 3.1 Captura padrão — `scripts/pncp_capture.py`

A documentação descreve entrada por URL pública do PNCP e geração de relatório Markdown, CSV de itens e JSON bruto, com opção de descarregar documentos e publicar relatórios textuais no GitHub mediante variável de ambiente `GITHUB_TOKEN`.

O código examinado valida o domínio e o formato do URL, consulta endpoints, tenta extrair metadados e links HTML e normaliza campos de itens. O próprio README lista limitações: páginas dependentes de JavaScript, disponibilidade/restrições da API e necessidade de parsing/OCR separado para anexos.

**Risco a testar:** o extrator heurístico e a identificação de endpoints não demonstram, por si só, que todas as páginas, itens, documentos ou paginações sejam capturados. Validar sempre contra o registo oficial e seus totais.

### 3.2 Captura integral — `scripts/pncp_capture_integral.py`

O código/documentação prevê captura de respostas de API e navegador Playwright, HTML/texto, links, itens, documentos e referências a atas, contratos, empenhos e histórico. Pode produzir JSON bruto, CSV de campos e relatório Markdown, com download opcional.

A documentação alerta expressamente que rotas, paginação e secções podem variar e que uma resposta HTTP com erro não significa que a secção esteja vazia. O download de anexos não extrai automaticamente texto/tabelas nem executa OCR.

**Risco a testar:** dependência de estrutura interna da página, permissões e comportamento variável do PNCP; estabelecer timeouts, retries controlados, paginação verificada, limites e relatórios de cobertura.

### 3.3 Calculadora de viabilidade — `scripts/calculadora_viabilidade.py`

Usa `Decimal` para calcular receita, aquisição, imposto incremental fornecido como parâmetro, DAS alocado, frete, entrega local, manuseamento, custos financeiros, outros custos, contingência, lucro, margem sobre receita, markup e teto de aquisição compatível com a margem alvo.

A recomendação é bloqueada enquanto houver pendências críticas de imposto, frete, conformidade técnica ou capacidade do fornecedor. A ferramenta documenta que não substitui validação fiscal profissional.

**Pontos a testar/rever:**
- comportamento com custo total ou receita nulos e valores de fronteira;
- consistência do arredondamento conservador no teto unitário e total;
- semântica de imposto percentual sobre receita e tratamento de DAS para evitar dupla contagem;
- persistência e ligação do cenário ao registo de cotação e à decisão;
- ausência de preço de aquisição confirmado deve continuar explicitamente assinalada como hipótese.

### 3.4 Schemas e exemplos

Foram identificados schemas JSON para:
- oportunidade;
- item;
- cotação;
- decisão;
- documento;
- cenário económico.

Há exemplos JSON de oportunidade e item para um processo da UFRJ. Existe `scripts/validate_schemas.py` para validar os schemas e exemplos e verificar um cálculo aritmético de referência.

O script de validação de schemas contém mapeamento explícito para exemplos cujo nome contém `oportunidade` ou `item`; outros tipos de exemplos podem gerar erro por ausência de mapeamento. O resultado efetivo da execução não foi verificado nesta auditoria estática.

### 3.5 CI e automação de repositório

Foram encontrados quatro workflows:
- `.github/workflows/auto-approve-docs.yml`;
- `.github/workflows/auto-cleanup-merged-pr.yml`;
- `.github/workflows/validacao.yml`;
- `.github/workflows/validate-governance.yml`.

Existência de workflows não prova que a aplicação comercial está testada. É necessário inspecionar os comandos, gatilhos e resultados recentes para saber exatamente quais verificações são executadas e se os testes de captura/calculadora fazem parte da CI.

## 4. Diagnóstico de maturidade

| Camada | Maturidade observada | Pode ser considerada pronta? |
|---|---|---|
| Governança documental | Estruturada, com pendências de revisão/aceitação registadas | Parcialmente |
| Arquivos de trabalho comercial | Diretórios dedicados existem | Não sem inventário do conteúdo |
| Contratos de dados | Schemas e exemplos presentes | Base inicial, não integração concluída |
| Captura de oportunidades | Scripts implementados | Não para produção sem testes de cobertura e falhas |
| Cálculo de viabilidade | Calculadora e testes de unidade escritos | Não até executar testes e rever casos fiscais/financeiros |
| Motor de decisão integrado | Schema e cálculo existem, integração não demonstrada | Não |
| Persistência transacional | Não encontrada evidência de banco de dados ou camada de repositório de negócio | Não |
| API/serviço de aplicação | Não encontrada evidência de serviço de negócio | Não |
| Dashboard de licitações | Não encontrado; existe SVG de status do projeto | Não |
| Observabilidade da aplicação | WATCHDOG documental e inventário de controlos; operação não comprovada | Não |

## 5. Prioridades recomendadas

### P0 — Reprodutibilidade e testes
1. Executar os testes unitários da calculadora num checkout limpo.
2. Executar `python scripts/validate_schemas.py` com a dependência `jsonschema`.
3. Verificar se a CI executa estes comandos e adicionar testes à CI se estiverem ausentes.
4. Corrigir falhas antes de usar a calculadora para decisões comerciais.

### P1 — Contrato de dados e persistência
1. Rever schemas contra casos reais do PNCP e os exemplos atuais.
2. Completar os schemas de fornecedor, resultado e contrato, se não estiverem cobertos noutros ficheiros.
3. Definir chaves de idempotência para oportunidade e item, histórico de alterações e ligações a documentos/cotações.
4. Escolher e documentar persistência antes de criar a interface.

### P2 — Testes da captura
1. Testar uma contratação com poucos itens e outra com múltiplas páginas/documentos.
2. Comparar contagens e campos com a fonte oficial e guardar relatório de cobertura.
3. Testar falha de rede, HTTP não-2xx, JSON inválido, timeout, repetição e URL não permitido.
4. Garantir que captura parcial fica marcada como parcial, nunca como completa.

### P3 — Motor de decisão e interface
1. Definir política de margem e bloqueios com aprovação do responsável.
2. Separar viabilidade financeira, conformidade técnica, habilitação e capacidade logística.
3. Expor resultados através de uma camada de aplicação que use os mesmos schemas e regras.
4. Só depois construir o dashboard comercial.

## 6. Critérios de saída da auditoria

- [ ] Testes unitários executados e resultado arquivado.
- [ ] Schemas e exemplos validados sem erros.
- [ ] CI inspecionada e cobertura de testes confirmada.
- [ ] Captura PNCP validada contra pelo menos dois casos reais e seus totais oficiais.
- [ ] Falhas, paginação, deduplicação e reexecução documentadas.
- [ ] Política de custo/margem e critérios de bloqueio aprovados.
- [ ] Decisão de persistência e arquitetura de aplicação documentada.
- [ ] Informação comercial confidencial excluída do repositório público ou protegida conforme política.

## 7. Limitações da auditoria

Esta é uma auditoria estática do conteúdo do repositório no commit indicado. Não foi executado código num checkout, não foram chamadas as APIs do PNCP a partir dos scripts, não foi confirmada a completude de documentos de editais, e não foi feita revisão fiscal/jurídica. Estados como “presente” significam que ficheiros/código foram encontrados, não que estejam operacionalmente aceites.

## 8. Fontes internas

- [README](../../README.md)
- [Scripts](../../scripts/README.md)
- [Calculadora de viabilidade](../../scripts/README-calculadora-viabilidade.md)
- [Captura integral](../../scripts/README-captura-integral.md)
- [Schemas](../../ARQUITETURA/schemas/)
- [Roadmap](../../ROADMAP-PADRAO-GOVERNANCA.md)
- [Registo de status](../../registry/status-do-projeto.json)
