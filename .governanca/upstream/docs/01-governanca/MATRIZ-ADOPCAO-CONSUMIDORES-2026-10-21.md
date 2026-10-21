# Matriz de adoção dos consumidores — GOVERNANCA

| Campo | Valor |
|---|---|
| ID | GOV-ADOPTION-MATRIX-001 |
| Data da inspeção | 2026-10-21 |
| Fonte canónica de âmbito | `registry/repositorios-consumidores.json` |
| Política de distribuição | `pull_request_only` |
| Estado | INVENTÁRIO RECONCILIADO; ACEITAÇÕES INDIVIDUAIS PENDENTES |

## 1. Critério de classificação

- **PILOTO_DIAGNOSTICO_PASS / CONFORMIDADE_UNKNOWN**: configuração e piloto técnico existem, mas não demonstram adoção normativa global.
- **SEM_CONFIG_LOCAL / UNKNOWN**: não foi encontrado o diretório `.governanca` na branch `main`; não há evidência local de integração do Governance Integration Framework.
- **DESATIVADO**: consumidor não pode receber distribuição automática até aprovação individual.
- **PASS de adoção** exige configuração local, ref imutável, execução do motor, relatório/hash, revisão humana, PR real e aceitação registada. A mera presença no registo de consumidores não é aceitação.

## 2. Matriz reconciliada

| Repositório | `enabled` no registo | Evidência observada em `main` | Estado de adoção | Próxima ação obrigatória |
|---|---:|---|---|---|
| [B3](https://github.com/carlos-andrade/B3) | true | Não encontrado `.governanca/` na raiz | UNKNOWN — sem configuração local do GIF | Criar configuração local por PR, fixar ref, executar motor e obter aceitação do proprietário; manter WATCHDOG separado até aceitação operacional |
| [DECIO-BAZIN](https://github.com/carlos-andrade/DECIO-BAZIN) | true | Não encontrado `.governanca/` na raiz | UNKNOWN — sem configuração local do GIF | Criar configuração local por PR e executar validação de perfil |
| [XFI](https://github.com/carlos-andrade/XFI) | true | Não encontrado `.governanca/` na raiz | UNKNOWN — sem configuração local do GIF | Criar configuração local por PR e executar validação de perfil |
| [CONSORCIO](https://github.com/carlos-andrade/CONSORCIO) | true | Não encontrado `.governanca/` na raiz | UNKNOWN — sem configuração local do GIF | Criar configuração local por PR e executar validação de perfil |
| [STOCKS](https://github.com/carlos-andrade/STOCKS) | true | [`.governanca/config.yml`](https://github.com/carlos-andrade/STOCKS/blob/main/.governanca/config.yml), blob SHA `c4f1ea14e4d0f174f8130510a11b435ae1998e43`; `modo: diagnostico`, `perfil: dados`, `exigir_pull_request: true`, `ref: c9be6d5224c7b412aa78a2b1d417b8315e5730f1` | PILOTO_DIAGNOSTICO_PASS / CONFORMIDADE_UNKNOWN | Revalidar o ref/relatório atual, executar distribuição real por PR e obter aceitação do proprietário; não promover a PASS global |
| [TURISTURIS](https://github.com/carlos-andrade/TURISTURIS) | true | Não encontrado `.governanca/` na raiz | UNKNOWN — sem configuração local do GIF | Criar configuração local por PR e executar validação de perfil |
| [BLOOMBERG_MAIL](https://github.com/carlos-andrade/BLOOMBERG_MAIL) | true | Não encontrado `.governanca/` na raiz | UNKNOWN — sem configuração local do GIF | Criar configuração local por PR e executar validação de perfil |
| [BRICKMASTER_GERAL](https://github.com/carlos-andrade/BRICKMASTER_GERAL) | true | Não encontrado `.governanca/` na raiz | UNKNOWN — sem configuração local do GIF | Criar configuração local por PR e executar validação de perfil |
| [LICITACAO](https://github.com/carlos-andrade/LICITACAO) | false | Existe espelho `.governanca/upstream/` e `UPSTREAM-MANIFEST.json` (blob SHA `bd7c33b95fa853ba2b44142a49ef9e53cbf61072`); o destino está desativado no registo central | DESATIVADO — não é adoção aceite | Manter `enabled: false`; só considerar reativação após aprovação local e piloto real por PR |

## 3. Conclusão

- Consumidores ativos registados: 8.
- Adoção global demonstrada: 0.
- Piloto técnico de diagnóstico conhecido: STOCKS, sem certificação global.
- Consumidor desativado: LICITACAO.
- Resultados UNKNOWN: B3, DECIO-BAZIN, XFI, CONSORCIO, STOCKS (conformidade global), TURISTURIS, BLOOMBERG_MAIL e BRICKMASTER_GERAL.

A matriz de inventário fica reconciliada com o registo e com a presença/ausência de configuração observada. **A adoção transversal não fica aprovada**: os consumidores ativos sem configuração continuam bloqueados para certificação; o destino LICITACAO permanece desativado. Cada aceitação exige evidência própria do repositório consumidor.

## 4. Evidências de referência

- [Registo canónico de consumidores](https://github.com/carlos-andrade/GOVERNANCA/blob/main/registry/repositorios-consumidores.json)
- [Relatório do piloto F3 — STOCKS](https://github.com/carlos-andrade/GOVERNANCA/blob/main/docs/01-governanca/RELATORIO-PILOTO-F3-STOCKS.md)
- [Pacote de aceitação e fecho](https://github.com/carlos-andrade/GOVERNANCA/blob/main/governanca/PACOTE-ACEITACAO-E-FECHO.md)
- [PR #4 — LICITACAO desativado no registo](https://github.com/carlos-andrade/GOVERNANCA/pull/4)
