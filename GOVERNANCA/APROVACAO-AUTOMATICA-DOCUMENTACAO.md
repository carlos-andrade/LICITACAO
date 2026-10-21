# Aprovação automática de documentação de baixo risco

## Objetivo
Reduzir espera operacional para alterações estritamente documentais sem remover os controles de merge do repositório.

## Escopo permitido
A automação só pode aprovar pull requests que:
- não estejam em rascunho;
- contenham exclusivamente arquivos Markdown (`.md`) em `EDITAIS/` e/ou `FORNECEDORES/`;
- não incluam arquivos removidos;
- não tenham sido criadas pela identidade configurada para o bot.

Qualquer arquivo fora dessas condições impede a aprovação automática. Alterações de workflow, código, configuração ou governança permanecem fora do escopo.

## Segurança e limites
- O workflow proposto usa `pull_request_target` para obter permissões de revisão, mas não deve fazer checkout nem executar código da branch da pull request.
- O token deve ser usado apenas para consultar arquivos/revisões e criar uma revisão de aprovação.
- Não habilitar auto-merge, não alterar rulesets e não contornar verificações obrigatórias.
- A aprovação não valida preços, cotações, fontes, conformidade jurídica, especificações técnicas ou habilitação de fornecedores.
- O merge continua sujeito aos checks e às proteções vigentes no repositório.

## Configuração necessária
Em **Settings → Secrets and variables → Actions**:
1. Criar o secret `LICITACAO_REVIEW_TOKEN` com um token dedicado, de privilégio mínimo e com permissão para criar revisões de pull request.
2. Criar a variável `LICITACAO_AUTOREVIEW_BOT` com o login exato da conta que fará a revisão.
3. Confirmar que a identidade do token corresponde ao bot configurado e que as regras de proteção aceitam essa revisão.

Não gravar tokens no repositório, em arquivos, comentários ou logs.

## Validação operacional
- O workflow `validate-governance.yml` valida alterações de governança, documentos de edital/fornecedores e workflows.
- O workflow de aprovação não se executa para a própria PR que introduz o arquivo pela primeira vez, pois `pull_request_target` utiliza a versão do workflow da branch base. Após merge aprovado, testar com uma PR documental elegível.
- Antes da ativação operacional, verificar os checks, os logs de Actions e a configuração dos secrets/variables. A presença do arquivo não comprova que esses valores estejam configurados.

## Estado
Proposta submetida a revisão. A automação só estará ativa após aprovação e merge da proposta do workflow e configuração dos secrets/variables.
