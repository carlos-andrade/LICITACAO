# Auditoria final de conformidade documental — LICITAÇÃO

| Campo | Valor |
|---|---|
| **ID** | LIC-AUD-FINAL-2026-10-22-001 |
| **Projeto** | LICITAÇÃO |
| **Repositório** | [carlos-andrade/LICITACAO](https://github.com/carlos-andrade/LICITACAO) |
| **Tipo documental** | AUDITORIA FINAL |
| **Fase** | Verificação de automação, inventário e anexos |
| **Estado** | EM_REVISAO |
| **Versão** | 1.0.0 |
| **SHA-256 (conteúdo canónico)** | b834bee2344171c0817fd64fcfba69f31dfdb197ead059b67042e24224dbb824 |
| **Commit de referência (versão anterior)** | [8572920cc2bf0521688794b71d1e672ab044369c](https://github.com/carlos-andrade/LICITACAO/commit/8572920cc2bf0521688794b71d1e672ab044369c) |
| **Data de criação** | 2026-10-22 |
| **Data de atualização** | 2026-10-22 |
| **Responsável** | Responsável pelo projeto LICITAÇÃO |
| **Aprovador** | Pendente — não há aprovação substantiva demonstrada |
| **Origem** | Execução do GitHub Actions, inventário versionado e inspeção dos três anexos recebidos nesta conversa |
| **Autoridade superior** | [Constituição do projeto](https://github.com/carlos-andrade/LICITACAO/blob/main/CONSTITUICAO.md) |
| **Cadeia de autoridade** | PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO |

## 1. Resultado do workflow

- Workflow [Validacao do Sistema LICITACAO](https://github.com/carlos-andrade/LICITACAO/actions/runs/39793338249): **concluído com sucesso**.
- Commit de disparo: `b5e445630ceaf57fac58be0d9022698169d1f41e` não; SHA observado no workflow: `b5e445630ceaf57fac58be0d9022698169d1f41e` não corresponde ao commit real. SHA correto do commit de disparo: `b5e445630ceaf57fac58be0d9022698169d1f41e`? 
- Etapas verificadas como concluídas: normalização de cabeçalhos e geração do inventário; publicação da normalização; testes unitários; validação de schemas e exemplos.
- O workflow criou e publicou o commit [8572920cc2bf0521688794b71d1e672ab044369c](https://github.com/carlos-andrade/LICITACAO/commit/8572920cc2bf0521688794b71d1e672ab044369c), com a mensagem “docs: normalizar cabeçalhos e inventariar conformidade documental”.

## 2. Inventário Markdown

Inventário gerado: [INVENTARIO-CONFORMIDADE-DOCUMENTAL.md](https://github.com/carlos-andrade/LICITACAO/blob/main/docs/governanca/INVENTARIO-CONFORMIDADE-DOCUMENTAL.md).

Resultados do inventário produzido pelo workflow:
- Markdown próprio do projeto: **42**.
- Cabeçalho e SHA-256 validados pelo script: **42/42**.
- IDs duplicados reportados: **0**.
- Markdown espelhado em `.governanca/upstream/`: **72**, auditado sem reescrita automática.
- PDF/Office versionados no repositório na execução: **0**.

O resultado confirma as verificações estruturais do script, não a correção substantiva de cada conteúdo nem a aprovação formal de documentos. Datas históricas não verificadas não foram inferidas.

## 3. Anexos recebidos diretamente na conversa

Foram inspecionados dois PDFs e uma planilha XLSX. Nenhum estava versionado no repositório, portanto o workflow não os modificou.

| Anexo original | ID de controlo | Verificação |
|---|---|---|
| Proposta comercial LV Consultoria (PDF) | `LIC-BIN-PROPOSTA-LV-001` | Criada cópia com folha de rosto de controlo; páginas originais mantidas a seguir |
| Certificado CCMEI atualizado (PDF) | `LIC-BIN-CCMEI-001` | Criada cópia com folha de rosto de controlo; páginas originais mantidas a seguir |
| Estudo de preços e viabilidade PMESP (XLSX) | `LIC-BIN-XLSX-PMESP-001` | Criada folha “CONTROLE DOCUMENTAL”; conteúdo das células das quatro folhas originais comparado e sem alterações |

As cópias revistas foram geradas nesta conversa para entrega separada. **Ainda não estão publicadas no GitHub**; esta auditoria não declara o contrário. Para que a exigência de armazenamento integral no repositório fique concluída, as três cópias revistas precisam ser adicionadas ao GitHub em operação de publicação de binários.

### SHA-256 dos ficheiros originais recebidos

- Proposta comercial: `3cabfee40ec3119738232e368e7fdc8f769b4cc72cb18e3856bcd24501984733`
- CCMEI: `056133e4addf25885f070ceca227132d79363aa7421a1b92ded57291dee22cf2`
- Planilha PMESP: `e030597e7d12c663e8b2e9f709b46ddb8236b0599433c8eb777d54da47e8a337`

Esses hashes identificam os ficheiros originais antes da inclusão do cabeçalho visual. Os hashes dos ficheiros revistos são diferentes, por definição.

## 4. Pendências residuais

1. Publicar no repositório as três cópias binárias revistas; a automação Markdown não realiza essa operação.
2. Após publicação, registar os hashes dos ficheiros publicados e validar os objetos efetivamente armazenados no GitHub.
3. Manter o estado `EM_REVISAO` até que a aprovação substantiva seja formalmente evidenciada.
