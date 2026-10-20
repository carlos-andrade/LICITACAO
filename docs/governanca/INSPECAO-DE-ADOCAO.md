# Inspeção de adoção da GOVERNANCA — LICITACAO

| Campo | Valor |
|---|---|
| **ID** | LIC-GOV-INSPEC-001 |
| **Projeto** | LICITACAO |
| **Repositório** | [carlos-andrade/LICITACAO](https://github.com/carlos-andrade/LICITACAO) |
| **Tipo documental** | RELATORIO_DE_INSPECAO |
| **Fase** | Adoção de governança |
| **Estado** | EM_REVISAO |
| **Versão** | 0.1.0 |
| **SHA-256 (conteúdo canónico)** | A_CALCULAR |
| **Commit de referência (versão anterior)** | [f42637de27d382049109e30bb7f05008815d45ef](https://github.com/carlos-andrade/LICITACAO/commit/f42637de27d382049109e30bb7f05008815d45ef) |
| **Data de criação** | 2026-10-20 |
| **Data de atualização** | 2026-10-20 |
| **Responsável** | Responsável pelo repositório — nomeação formal pendente |
| **Aprovador** | Pendente |
| **Origem** | Inspeção documental inicial das referências públicas da GOVERNANCA e do LICITACAO |
| **Autoridade superior** | [GOVERNANCA/CONSTITUICAO.md](https://github.com/carlos-andrade/GOVERNANCA/blob/main/CONSTITUICAO.md) |
| **Cadeia de autoridade** | PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO |

## Resumo

Esta inspeção orienta a preparação do LICITACAO. Não equivale à certificação de conformidade. A GOVERNANCA exige inspeção individual por repositório e deixa claro que a referência às normas ou o espelhamento não prova adoção.

## Evidência de origem verificada

- [Constituição canónica](https://github.com/carlos-andrade/GOVERNANCA/blob/main/CONSTITUICAO.md) — princípios, hierarquia, gates e WATCHDOG.
- [Carta/Contrato do roadmap](https://github.com/carlos-andrade/GOVERNANCA/blob/main/CARTA-CONTRATO-PADRAO-ROADMAP.md) — adoção individual, fail-closed e evidências.
- [Roadmap padrão](https://github.com/carlos-andrade/GOVERNANCA/blob/main/ROADMAP-PADRAO-GOVERNANCA.md) — formato de plano executivo.
- [Norma de status](https://github.com/carlos-andrade/GOVERNANCA/blob/main/standards/status-e-percentual-de-conclusao.md) — pontos, scorecard e evidências.
- [Norma de cabeçalho](https://github.com/carlos-andrade/GOVERNANCA/blob/main/CABE%C3%87ALHO/NORMA-CABECALHO-PADRAO.md) — metadados visíveis Markdown.
- [WATCHDOG](https://github.com/carlos-andrade/GOVERNANCA/blob/main/WATCHDOG/README.md) — estados, limites e critério de adoção.
- [Registo dos repositórios consumidores](https://github.com/carlos-andrade/GOVERNANCA/blob/main/registry/repositorios-consumidores.json) — LICITACAO não consta da lista de consumidores ativos observada.

## Resultado da inspeção inicial

| Controlo | Resultado | Evidência/ação necessária |
|---|---|---|
| Repositório acessível | PASS | Consultas públicas do GitHub responderam |
| README com objetivo | WARN | README inicial é mínimo; atualizar com links e estado |
| Constituição local | PENDENTE | Criada nesta branch; requer revisão e aprovação |
| Carta e roadmap | PENDENTE | Criados nesta branch; verificar cabeçalhos, critérios e links |
| Scorecard canónico | PENDENTE | JSON inicial criado com zero pontos; validar sintaxe e regras |
| WATCHDOG local | PENDENTE | Registos iniciais criados; precisam de validação automatizada |
| CI executada com sucesso | UNKNOWN | Sem execução bem-sucedida confirmada nesta preparação |
| Proteção de branch | UNKNOWN | Verificar e configurar regras no GitHub |
| Monitorização externa independente | UNKNOWN | Exige implementação, ligação e teste; não está ativa por esta inspeção |
| Propagação automática upstream | BLOQUEADO/UNKNOWN | GOVERNANCA documenta falha anterior do token de sincronização; revalidar credencial sem a revelar |
| Adoção formal | EM_REVISAO | Aprovação explícita e critérios acima pendentes |

## Decisão recomendada

**Não declarar adoção concluída.** Manter estado `EM_REVISAO` até que:
1. o README esteja ligado aos documentos locais;
2. o scorecard e o inventário WATCHDOG passem validações automatizadas;
3. haja execução CI bem-sucedida e evidência arquivada;
4. proteção de branch e política de revisão sejam verificadas;
5. a adoção local seja revista e aprovada pelo responsável autorizado;
6. a referência à GOVERNANCA e, se ativada, a sincronização upstream sejam verificadas.

## Próxima ação

Validar este pacote documental em Pull Request, executar verificações automatizadas e obter revisão/aceitação explícita antes de iniciar a estrutura funcional. Não fazer merge nem alterar os conteúdos canónicos da GOVERNANCA neste passo.
