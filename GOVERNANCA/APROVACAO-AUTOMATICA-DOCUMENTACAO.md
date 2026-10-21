# Política de aprovação automática — documentação de baixo risco

## Objetivo

Reduzir a espera por revisão manual em alterações documentais rotineiras sem desativar as proteções da branch main nem aprovar mudanças funcionais ou de governança por engano.

## Escopo elegível

O workflow .github/workflows/auto-approve-docs.yml pode aprovar automaticamente uma PR somente quando todos os arquivos alterados forem arquivos Markdown não removidos dentro de:

- EDITAIS/
- FORNECEDORES/

Alterações fora desse escopo não recebem aprovação automática. Em especial, ficam excluídos código, scripts, dependências, workflows, regras de proteção, documentos de governança na raiz, segredos e configurações.

## Requisitos técnicos

1. Configurar o segredo de repositório LICITACAO_REVIEW_TOKEN com um token de uma GitHub App ou conta-bot dedicada, com permissão mínima para ler conteúdo e criar revisões de PR.
2. Configurar a variável de repositório LICITACAO_AUTOREVIEW_BOT com o login exato dessa App/bot.
3. O token precisa pertencer a uma identidade diferente do autor da PR; a automação não aprova PRs criadas pela própria identidade bot.
4. Manter os checks obrigatórios. Uma aprovação não substitui testes, validações nem regras de merge.
5. Testar primeiro em PRs documentais de baixo risco e confirmar se a identidade do bot satisfaz a regra de aprovação configurada no repositório.

## Limites e controles

- O workflow usa pull_request_target para operar sobre metadados da PR, não faz checkout nem executa código da branch proposta.
- A lista de arquivos é verificada no GitHub API; qualquer arquivo fora da allowlist bloqueia a aprovação automática.
- A aprovação não significa validação factual de preços, cotações, fontes, especificações oficiais, habilitação ou conformidade jurídica.
- Não habilitar auto-merge nem ignorar rulesets como parte desta automação.
- Mudanças nas regras de governança, nos workflows ou no código exigem revisão conforme a política do repositório.
- Se a configuração de regras exigir um tipo de revisor que não aceite a identidade bot, o workflow não remove essa exigência; a regra deve ser ajustada conscientemente nas configurações do GitHub por um administrador autorizado.

## Ativação

Após a PR ser revisada e mesclada, configurar os dois valores de repositório acima em Settings → Secrets and variables → Actions. Sem o segredo e a variável, o workflow não aprovará PRs. Não armazenar tokens no repositório nem em arquivos de documentação.
