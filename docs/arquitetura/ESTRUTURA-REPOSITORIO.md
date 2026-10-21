# Estrutura inicial do repositório LICITACAO

**Estado:** proposta documental; não constitui autorização para ativar módulos funcionais.

## Princípios

- O repositório de destino é `carlos-andrade/LICITACAO`.
- A governança normativa continua subordinada ao repositório GOVERNANCA.
- O Gate G0 permanece bloqueado até existir evidência formal verificável de aprovação.
- `LICITACAO.enabled` deve permanecer `false` até aprovação individual e validação operacional da distribuição por pull request.
- Não implementar integrações, automações de negócio, persistência operacional ou execução de processos antes da liberação formal.

## Árvore proposta

```text
LICITACAO/
├── .github/
│   ├── ISSUE_TEMPLATE/
│   └── PULL_REQUEST_TEMPLATE.md
├── docs/
│   ├── arquitetura/
│   │   ├── ESTRUTURA-FUNCIONAL-MODULOS-FLUXOS.md
│   │   └── ESTRUTURA-REPOSITORIO.md
│   ├── governanca/
│   ├── processos/
│   ├── seguranca/
│   └── operacao/
├── schemas/                 # reservado; definir após G0
├── src/                     # reservado; sem código funcional antes de G0
│   ├── core/                # reservado
│   ├── modules/             # reservado
│   ├── integrations/        # reservado
│   └── api/                 # reservado
├── tests/                   # reservado; plano de testes pode ser documentado
├── scripts/                 # reservado; não adicionar automações operacionais antes de G0
├── .gitignore
└── README.md
```

## Responsabilidade das áreas

| Área | Responsabilidade prevista | Estado atual |
|---|---|---|
| `.github/` | Modelos de contribuição e revisão por PR | Pode receber configuração documental, sujeita às regras do repositório |
| `docs/arquitetura/` | Arquitetura, módulos, fluxos e decisões técnicas | Permitido como documentação proposta |
| `docs/governanca/` | Evidências, gates, responsabilidades e decisões | Apenas registos verificáveis; não substituir o repositório normativo |
| `docs/processos/` | Procedimentos de negócio e exceções | Documentação proposta |
| `docs/seguranca/` | Modelo de ameaças, acessos e tratamento de dados | Documentação proposta |
| `docs/operacao/` | Operação, observabilidade e resposta a incidentes | Documentação proposta |
| `schemas/` | Contratos e modelos de dados | Bloqueado até G0 |
| `src/` | Implementação dos módulos e interfaces | Bloqueado até G0 |
| `tests/` | Testes executáveis e validação funcional | Bloqueado até G0; critérios podem ser documentados |
| `scripts/` | Ferramentas de execução e automação | Bloqueado até G0 |

## Sequência de habilitação

1. Formalizar e registar a evidência de aprovação do Gate G0.
2. Validar o mecanismo de distribuição por pull request e as verificações obrigatórias.
3. Aprovar individualmente o módulo ou incremento proposto, com critérios de aceitação e responsável.
4. Implementar apenas o escopo aprovado, em branch própria e por pull request.
5. Executar verificações, obter revisão independente e registar evidências.
6. Ativar funcionalidades somente após cumprir os controlos de governança aplicáveis.

## Fora de escopo neste momento

Este documento não cria diretórios de código, não implementa módulos M00–M13, não ativa funcionalidades e não altera configurações ou registos do repositório GOVERNANCA. A árvore é uma proposta para orientar a evolução controlada do repositório; a criação de código funcional depende dos gates acima.
