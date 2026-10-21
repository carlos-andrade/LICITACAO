# Roadmap — LICITACAO sob a GOVERNANCA

| Campo | Valor |
|---|---|
| **ID** | LIC-GOV-ROADMAP-001 |
| **Projeto** | LICITACAO |
| **Repositório** | [carlos-andrade/LICITACAO](https://github.com/carlos-andrade/LICITACAO) |
| **Tipo documental** | ROADMAP |
| **Fase** | Adoção de governança |
| **Estado** | APROVADO_COM_LIMITACOES |
| **Versão** | 0.1.0 |
| **SHA-256 (conteúdo canónico)** | PENDENTE — calcular após validação final do conteúdo |
| **Commit de referência (versão anterior)** | [f42637de27d382049109e30bb7f05008815d45ef](https://github.com/carlos-andrade/LICITACAO/commit/f42637de27d382049109e30bb7f05008815d45ef) |
| **Data de criação** | 2026-10-20 |
| **Data de atualização** | 2026-10-20 |
| **Responsável** | Proprietário do repositório LICITACAO |
| **Aprovador** | Carlos Andrade — decisão de adoção registada em 2026-10-21 |
| **Origem** | Adaptação do [Roadmap padrão aprovado da GOVERNANCA](https://github.com/carlos-andrade/GOVERNANCA/blob/main/ROADMAP-PADRAO-GOVERNANCA.md) |
| **Autoridade superior** | [Constituição local](CONSTITUICAO.md) e Carta/Contrato de adoção local |
| **Cadeia de autoridade** | PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO |

## Painel executivo

- **Objetivo:** preparar uma base governada para o futuro sistema de inteligência comercial e apoio ao fornecimento em contratações públicas brasileiras.
- **Estado:** APROVADO_COM_LIMITACOES — G0 aprovado e distribuição upstream validada; WATCHDOG não operacional.
- **Fase atual:** Início / adoção de governança.
- **Percentual comprovado:** 0% até existir um scorecard validado; não confundir criação de ficheiros com controlo aceite.
- **Próximo marco:** avançar para G1 — viabilidade, com análise de fontes, procura, custo total, margem, risco e dependências; ativação de distribuição será formalizada na GOVERNANCA por PR #32.
- **Bloqueios:** a distribuição automática da GOVERNANCA depende de credencial válida e operação comprovada; o repositório mestre documenta falha de autenticação anterior. Não afirmar sincronização automática ativa.
- **Riscos principais:** adoção meramente documental; regras upstream desatualizadas; exposição indevida de informação comercial; preços calculados com custos incompletos; dependência de fontes externas; falta de cobertura de testes.
- **Evidência central:** [GOVERNANCA — Carta/Contrato](https://github.com/carlos-andrade/GOVERNANCA/blob/main/CARTA-CONTRATO-PADRAO-ROADMAP.md), [Roadmap padrão](https://github.com/carlos-andrade/GOVERNANCA/blob/main/ROADMAP-PADRAO-GOVERNANCA.md), [Constituição](https://github.com/carlos-andrade/GOVERNANCA/blob/main/CONSTITUICAO.md).

## Sequência de gates

| Gate | Objetivo | Entregáveis | Critério de saída | Estado |
|---|---|---|---|---|
| G0 | Registar propósito e propriedade | Charter, escopo inicial, owner e beneficiários | Propósito, owner, limites e critérios documentados | APROVADO |
| G1 | Validar viabilidade | Fontes oficiais, hipóteses de categorias, riscos, custos e dependências | Viabilidade com pressupostos e evidências | BLOQUEADO |
| G2 | Desenhar solução | Requisitos, arquitetura, modelo de dados, ameaças e testes | Revisão do desenho e critérios aprovados | NÃO_INICIADO |
| G3 | Construir e validar | Código, testes, documentação e rastreabilidade | Testes executados, revisão e evidências aceites | NÃO_INICIADO |
| G4 | Preparar operação | Segurança, credenciais, backups, monitorização, suporte e rollback | Checklist operacional aprovada | NÃO_INICIADO |
| G5 | Autorizar operação | Plano de ativação, métricas e rollback | Autorização explícita e observação pós-ativação | NÃO_INICIADO |
| G6 | Encerrar e transferir | Aceitação, documentação final, arquivo e lições | Aprovação formal de encerramento | NÃO_INICIADO |

Gates podem ser adaptados ao risco, mas obrigações legais, controlos críticos e evidências obrigatórias não podem desaparecer silenciosamente.

## Ações prioritárias

| Prioridade | Ação | Critério de conclusão | Estado |
|---|---|---|---|
| P0 | Rever pacote de governança local | Referências, cabeçalhos, estados e links verificados | CONCLUÍDO COM LIMITAÇÕES |
| P0 | Validar scorecard e registo canónico | Critérios e evidências; soma válida 20/60/20 | EM_CURSO |
| P0 | Inspecionar adoção | Resultado documentado e aprovação autorizada; sem presumir sincronização | APROVADO_COM_LIMITACOES |
| P1 | Validar WATCHDOG local | Sistemas, owners, criticidade e controlos testados | PENDENTE |
| P1 | Validar CI | Workflow executado com resultado acessível | PASS — run pós-merge 39623794138 |
| P2 | Estruturar aplicação e estratégia comercial | Somente depois do gate de governança e dos requisitos | BLOQUEADO |

## Critérios de aceitação desta fase

- [ ] Constituição local e referências canónicas publicadas.
- [ ] Roadmap ligado no README.
- [ ] Scorecard, pontuação e evidências validados.
- [ ] Gates G0–G6 e ações prioritárias mapeados.
- [ ] Inventário WATCHDOG revisto e validado.
- [ ] Segredos, licenças, permissões e proteção da branch verificados.
- [ ] CI executada e resultado arquivado.
- [ ] Inspeção local registada e adoção aprovada.

## Riscos e bloqueios

1. O projeto mestre reporta falha anterior de autenticação do token de distribuição; não declarar propagação operacional sem nova evidência.
2. Proteção da branch, revisão obrigatória e segregação precisam de verificação no GitHub.
3. Nenhuma recomendação de lance sem custos, requisitos e capacidade de entrega verificados.
4. Propostas reservadas, credenciais e dados pessoais não devem ser expostos no repositório público.
5. Estes documentos não substituem avaliação jurídica, fiscal ou revisão específica de cada edital.

## Histórico

| Versão | Data | Alteração | Evidência |
|---|---|---|---|
| 0.1.0 | 2026-10-20 | Roadmap inicial para adoção da governança | Branch de adoção; validação pendente |
