# Decisão de adoção da GOVERNANCA — LICITACAO

| Campo | Valor |
|---|---|
| **ID** | LIC-DOC-DOCS-GOVERNANCA-DECISAO-ADOCAO-GOVERNANCA-MD-DA483360 |
| **Projeto** | LICITAÇÃO |
| **Repositório** | [carlos-andrade/LICITACAO](https://github.com/carlos-andrade/LICITACAO) |
| **Tipo documental** | DOCUMENTO_TECNICO |
| **Fase** | N/A — fase não definida no conteúdo de origem |
| **Estado** | EM_REVISAO |
| **Versão** | 1.0.0 |
| **SHA-256 (conteúdo canónico)** | a3e4d71a8f2b5314819b108ee866cfb6e2ee6f3df8b05a429c76739f09b5a939 |
| **Commit de referência (versão anterior)** | [b5e445630ceaf57fac58ae963dbedc587d836e52](https://github.com/carlos-andrade/LICITACAO/commit/b5e445630ceaf57fac58ae963dbedc587d836e52) |
| **Data de criação** | N/A — data histórica não verificada |
| **Data de atualização** | 2026-10-22 |
| **Responsável** | Responsável pelo projeto LICITAÇÃO |
| **Aprovador** | Pendente — não há evidência de aprovação neste documento |
| **Origem** | Conteúdo existente no repositório; caminho: `docs/governanca/DECISAO-ADOCAO-GOVERNANCA.md` |
| **Autoridade superior** | [Constituição do projeto](https://github.com/carlos-andrade/LICITACAO/blob/main/CONSTITUICAO.md) |
| **Cadeia de autoridade** | PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO |

- **ID:** LIC-GOV-ADOCAO-001
- **Estado:** PROPOSTA FORMAL — AGUARDANDO APROVAÇÃO HUMANA
- **Repositório consumidor:** `carlos-andrade/LICITACAO`
- **Repositório normativo:** [`carlos-andrade/GOVERNANCA`](https://github.com/carlos-andrade/GOVERNANCA)
- **Política de distribuição:** `pull_request_only`
- **Data de preparação:** 2026-10-21

## 1. Decisão proposta

Propõe-se a adoção formal da GOVERNANCA como referência normativa para os controlos de governação aplicáveis ao repositório LICITACAO, sob as condições e limites definidos neste documento.

Este documento é uma proposta para decisão. A sua criação ou integração não equivale a aprovação humana. A adoção só passa a **APROVADA** depois de o aprovador autorizado registar a decisão nesta secção e a PR que a contém ser aprovada segundo as regras do repositório.

## 2. Responsabilidade e aprovação

- **Owner técnico do repositório:** Carlos Andrade (owner declarado no registo central; confirmar que esta atribuição continua válida).
- **Responsável pela decisão de adoção:** pendente de confirmação explícita.
- **Aprovador autorizado:** pendente de registo explícito de identidade e aprovação.
- **Data da aprovação:** pendente.
- **Evidência de aprovação:** link para a review APPROVE e para a PR integrada; pendente.

Não se presume que o autor desta proposta tenha autoridade para aprovar em nome de outra pessoa ou que uma PR integrada sem review constitua aprovação.

## 3. Políticas e controlos obrigatórios propostos

Após aprovação, LICITACAO compromete-se a:

1. Manter a Constituição, os padrões e os documentos normativos da GOVERNANCA como fonte de referência para a governação adotada.
2. Receber os espelhos publicados pela origem apenas no diretório isolado `.governanca/upstream/`; a publicação não deve sobrescrever documentos locais.
3. Aplicar revisão humana, verificações CI e regras de proteção de branch antes de integrar alterações.
4. Tratar o manifesto e o commit de origem como evidência de proveniência; verificar os diffs antes de aceitar uma atualização.
5. Manter a avaliação do Gate G0 separada da adoção da GOVERNANCA. A adoção não aprova G0 nem autoriza módulos funcionais.
6. Registar desvios, incidentes, exceções e decisões relevantes no repositório.

## 4. Limites de autoridade e exceções

- A GOVERNANCA pode propor atualizações normativas; não recebe autoridade para integrar automaticamente essas atualizações em LICITACAO.
- A automação de distribuição pode criar ou atualizar branches e Pull Requests, mas não pode fazer merge.
- O merge permanece sujeito às proteções do repositório de destino, às verificações obrigatórias e à aprovação humana exigida.
- Uma exceção deve ser específica, justificada, limitada no tempo e no âmbito, aprovada por responsável autorizado e registada por escrito. Não pode desativar proteções de branch nem converter a política de distribuição em escrita direta.
- Testes operacionais dirigidos a um repositório ainda desativado só podem usar um modo de teste explicitamente limitado a esse repositório. Esse modo não altera o estado de adoção nem habilita a distribuição geral.
- Em caso de falha, evidência incompleta ou divergência, prevalece o estado bloqueado (`fail-closed`).

## 5. Distribuição por Pull Request

A política obrigatória é `pull_request_only`. Cada atualização proveniente da GOVERNANCA deve ser proposta por PR no repositório consumidor. É proibido o merge automático.

A PR deve incluir, quando aplicável:
- commit exato da GOVERNANCA que serviu de origem;
- manifesto com os caminhos e hashes dos ficheiros publicados;
- diff revisto;
- resultado das verificações CI;
- indicação explícita de que a publicação não certifica, por si só, adoção ou conformidade.

## 6. Critérios para considerar a adoção aprovada

- [ ] Responsável pela decisão e aprovador autorizado identificados.
- [ ] Review humana APPROVE registada na PR desta decisão.
- [ ] PR da decisão integrada respeitando as regras do repositório.
- [ ] Teste operacional de distribuição por PR concluído e documentado.
- [ ] Confirmado que a PR de teste não foi integrada automaticamente.
- [ ] Registo central atualizado apenas por uma PR separada, depois de concluídas as condições anteriores.

## 7. Estado de adoção

**Estado atual: PENDENTE — NÃO TRATAR COMO APROVADA.**

A alteração de `enabled: false` para `enabled: true` no registo central não faz parte desta decisão e não deve ocorrer até existirem as evidências exigidas. A aprovação desta adoção também não desbloqueia o Gate G0 do projeto.

## 8. Evidências e ligações

- [Registo central de consumidores](https://github.com/carlos-andrade/GOVERNANCA/blob/main/registry/repositorios-consumidores.json)
- [Workflow de distribuição](https://github.com/carlos-andrade/GOVERNANCA/blob/main/.github/workflows/propagar-regras-governanca.yml)
- [Script de distribuição](https://github.com/carlos-andrade/GOVERNANCA/blob/main/automation/propagar_governanca.py)
- PR desta decisão: a preencher após abertura.
- PR de teste operacional: pendente.
- Execução do workflow e artefacto de relatório: pendentes.
