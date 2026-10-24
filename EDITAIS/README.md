# Editais

| Campo | Valor |
|---|---|
| **ID** | LIC-DOC-EDITAIS-README-MD-A7AD5675 |
| **Projeto** | LICITAÇÃO |
| **Repositório** | [carlos-andrade/LICITACAO](https://github.com/carlos-andrade/LICITACAO) |
| **Tipo documental** | README |
| **Fase** | N/A — fase não definida no conteúdo de origem |
| **Estado** | EM_REVISAO |
| **Versão** | 1.0.0 |
| **SHA-256 (conteúdo canónico)** | 9ad828851e60df64e8557a2dfe5a44cf1a627c6c315a2efd2938fdeed4541cff |
| **Commit de referência (versão anterior)** | [b5e445630ceaf57fac58ae963dbedc587d836e52](https://github.com/carlos-andrade/LICITACAO/commit/b5e445630ceaf57fac58ae963dbedc587d836e52) |
| **Data de criação** | N/A — data histórica não verificada |
| **Data de atualização** | 2026-10-24 |
| **Responsável** | Responsável pelo projeto LICITAÇÃO |
| **Aprovador** | Pendente — não há evidência de aprovação neste documento |
| **Origem** | Conteúdo existente no repositório; caminho: `EDITAIS/README.md` |
| **Autoridade superior** | [Constituição do projeto](https://github.com/carlos-andrade/LICITACAO/blob/main/CONSTITUICAO.md) |
| **Cadeia de autoridade** | PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO |

Diretório destinado à organização de documentos e registos relacionados com editais de concursos públicos.

## Regras de organização

- Manter cada edital identificado por órgão/entidade, número/ano e data de publicação, quando disponíveis.
- Separar documentos originais, análises e evidências em subdiretórios claramente identificados, conforme forem definidos.
- Preservar a origem e a integridade dos documentos; não substituir originais por cópias anotadas.
- Não incluir credenciais, segredos ou dados pessoais desnecessários.
- Até à aprovação formal do Gate G0, este diretório é apenas estrutura documental; não representa ativação de módulos funcionais.


## Coleta automatizada PNCP

A coleta dos editais com propostas abertas e modalidade código 8 está documentada em [README-CAPTURA-PNCP.md](README-CAPTURA-PNCP.md). O script está em [capture_pncp_editais.py](../scripts/capture_pncp_editais.py); o workflow é [Captura de editais PNCP](../.github/workflows/captura-pncp-editais.yml). Os arquivos de resultados só serão considerados preenchidos após uma execução com dados reais.


## Extrator de contratação específica

Para extração detalhada de uma contratação individual, consulte [o guia do extrator](EXTRATOR-CONTRATACAO-PNCP-00394502000144-2026-14259.md), o [script](../scripts/capture_pncp_contratacao.py) e o [workflow de execução](../.github/workflows/extrair-pncp-contratacao.yml).
