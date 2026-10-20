# LICITACAO — Governança e preparação do projeto

| Campo | Valor |
|---|---|
| **ID** | LIC-README-001 |
| **Projeto** | LICITACAO |
| **Repositório** | [carlos-andrade/LICITACAO](https://github.com/carlos-andrade/LICITACAO) |
| **Tipo documental** | README |
| **Fase** | Adoção de governança |
| **Estado** | EM_REVISAO |
| **Versão** | 0.2.0 |
| **SHA-256 (conteúdo canónico)** | PENDENTE — calcular após validação final do conteúdo |
| **Commit de referência (versão anterior)** | [f42637de27d382049109e30bb7f05008815d45ef](https://github.com/carlos-andrade/LICITACAO/commit/f42637de27d382049109e30bb7f05008815d45ef) |
| **Data de criação** | 2026-10-20 |
| **Data de atualização** | 2026-10-20 |
| **Responsável** | Proprietário do repositório LICITACAO |
| **Aprovador** | Pendente de aprovação formal |
| **Origem** | Expansão controlada do README inicial |
| **Autoridade superior** | [Constituição local](CONSTITUICAO.md) e [GOVERNANCA](https://github.com/carlos-andrade/GOVERNANCA) |
| **Cadeia de autoridade** | PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO |

> **Estado de governança: EM_REVISAO.** A adoção está em preparação; não é certificação nem declaração de conformidade completa.

![Painel visual de status](assets/status-dashboard.svg)

## Propósito

Preparar uma plataforma para identificar, analisar e acompanhar oportunidades de fornecimento de produtos a órgãos públicos brasileiros, com foco em decisões comerciais rastreáveis, custos completos, conformidade com os instrumentos convocatórios e preservação de capital.

## Governança primeiro

Antes da estrutura funcional, o projeto adota como referência a GOVERNANCA. A documentação local, os gates, o estado do projeto e as verificações precisam ser revistos e aceites individualmente.

- [Constituição local](CONSTITUICAO.md)
- [Carta/Contrato de adoção do roadmap](CARTA-CONTRATO-PADRAO-ROADMAP.md)
- [Roadmap](ROADMAP-PADRAO-GOVERNANCA.md)
- [Registo de status](registry/status-do-projeto.json)
- [Inspeção inicial de adoção](docs/governanca/INSPECAO-DE-ADOCAO.md)
- [Índice de governança](docs/governanca/README.md)
- [WATCHDOG local](WATCHDOG/README.md)
- [Espelho das referências canónicas](.governanca/upstream/UPSTREAM-MANIFEST.json)

## Direção comercial preliminar

- **Jurisdição:** Brasil.
- **Modelo:** revenda de produtos adquiridos de distribuidores, atacadistas e fabricantes.
- **Capital de giro de referência:** faixa informada de R$ 50 mil a R$ 200 mil; utilização efetiva dependerá de validação financeira.
- **Categorias:** pesquisa exploratória de múltiplas categorias, com foco definido por evidência de demanda, concorrência, fornecedores, logística e margem.
- **Fontes públicas de referência:** [PNCP](https://pncp.gov.br/app/editais), [Compras.gov.br — fornecedores](https://www.gov.br/compras/pt-br/fornecedor-1/fornecedor) e legislação vigente aplicável.

Nenhuma proposta, preço, fornecedor ou edital será considerado aprovado sem validação específica. Decisões finais de participação, lance, habilitação e execução contratual requerem revisão humana autorizada.

## Status de governança

O registo canónico é `registry/status-do-projeto.json`. O percentual deve ser calculado apenas a partir de critérios e evidências verificáveis segundo a norma de status da GOVERNANCA. O SVG é, nesta fase, uma representação provisória; automatizar sua geração a partir do registo é um critério de adoção pendente.

## Limitações atuais

Ainda não há aplicação de negócio implementada. O workflow de validação do bootstrap executou com sucesso no commit `965d1a2993e49cd5b0ae7a4dacca84226bb2e379` ([execução](https://github.com/carlos-andrade/LICITACAO/actions/runs/39449489411)); esse resultado cobre apenas as verificações implementadas no workflow e não equivale à aprovação formal da adoção. Segurança operacional, WATCHDOG e sincronização upstream continuam pendentes de verificação e evidência. Na leitura atual da API do GitHub, a branch `main` está sem proteção (`protected=false`; `protection.enabled=false`) e ainda precisa de regras obrigatórias de revisão e verificações. Não guardar credenciais, dados pessoais desnecessários ou informação comercial confidencial no repositório público.

## Próximo marco

Validar esta preparação documental em Pull Request, executar verificações automatizadas e obter revisão/aceitação explícita antes de iniciar a estrutura funcional.
