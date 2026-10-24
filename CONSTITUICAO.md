# Constituição local de governança — LICITACAO

| Campo | Valor |
|---|---|
| **ID** | LIC-GOV-CONST-001 |
| **Projeto** | LICITACAO |
| **Repositório** | [carlos-andrade/LICITACAO](https://github.com/carlos-andrade/LICITACAO) |
| **Tipo documental** | CONSTITUICAO_LOCAL |
| **Fase** | Adoção de governança |
| **Estado** | EM_REVISAO |
| **Versão** | 0.1.0 |
| **SHA-256 (conteúdo canónico)** | 0b5788c2058826cd7ec442be4b8a00402cae07c861d5651d01596e8cefb9d841 |
| **Commit de referência (versão anterior)** | [f42637de27d382049109e30bb7f05008815d45ef](https://github.com/carlos-andrade/LICITACAO/commit/f42637de27d382049109e30bb7f05008815d45ef) |
| **Data de criação** | 2026-10-20 |
| **Data de atualização** | 2026-10-24 |
| **Responsável** | Proprietário do repositório LICITACAO |
| **Aprovador** | Pendente de aprovação formal |
| **Origem** | Adaptação inicial das referências canónicas da GOVERNANCA |
| **Autoridade superior** | [GOVERNANCA/CONSTITUICAO.md](https://github.com/carlos-andrade/GOVERNANCA/blob/main/CONSTITUICAO.md), lei aplicável e contratos vinculativos |
| **Cadeia de autoridade** | PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO |

## 1. Finalidade

Preparar o repositório LICITACAO para receber a estrutura funcional de inteligência comercial, análise de oportunidades e apoio à participação em contratações públicas no Brasil. Esta constituição é uma adaptação local inicial e permanece em revisão; não declara adoção formal concluída nem conformidade jurídica certificada.

## 2. Princípios obrigatórios

1. **Evidência antes de alegação:** não declarar edital validado, fornecedor disponível, preço competitivo, teste executado ou controlo operacional sem referência verificável.
2. **Legalidade e integridade:** respeitar legislação, edital, contrato, segregação de funções e regras de integridade aplicáveis.
3. **Rastreabilidade:** ligar requisitos, documentos, decisões, cotações, cálculos, propostas, resultados e execução contratual.
4. **Segurança por conceção:** não guardar tokens, credenciais, dados pessoais desnecessários, documentos comerciais confidenciais ou segredos em Git.
5. **Proteção de caixa:** nenhuma proposta pode ser recomendada sem análise de custo completo, capital comprometido, prazo de entrega e risco de recebimento.
6. **Revisão humana:** decisões de participação, preço final, habilitação, assinatura e aceite contratual exigem decisão humana autorizada.
7. **Fail-closed:** dados ausentes, fonte indisponível, requisito ambíguo ou cálculo incompleto devem resultar em bloqueio, pendência ou UNKNOWN — nunca em sucesso presumido.
8. **Reversibilidade e histórico:** alterações relevantes preservam motivo, autor, data e evidência.
9. **Proporcionalidade:** intensidade de controle escala com risco jurídico, financeiro, operacional, de dados e de reputação.
10. **Independência da fonte:** esta adaptação local não substitui nem modifica as normas canónicas no repositório GOVERNANCA.

## 3. Hierarquia

A precedência é: (1) lei aplicável e regulamentos; (2) contratos e edital vinculativos; (3) políticas formalmente aprovadas; (4) Carta/Contrato e padrões adotados da GOVERNANCA; (5) procedimentos locais; (6) recomendações e exemplos. Conflitos devem ser registados e escalados, nunca resolvidos silenciosamente.

Referências canónicas: [Constituição](https://github.com/carlos-andrade/GOVERNANCA/blob/main/CONSTITUICAO.md), [Carta/Contrato de roadmap](https://github.com/carlos-andrade/GOVERNANCA/blob/main/CARTA-CONTRATO-PADRAO-ROADMAP.md), [Roadmap padrão](https://github.com/carlos-andrade/GOVERNANCA/blob/main/ROADMAP-PADRAO-GOVERNANCA.md), [norma de status](https://github.com/carlos-andrade/GOVERNANCA/blob/main/standards/status-e-percentual-de-conclusao.md).

## 4. Papéis e decisões

- **Patrocinador/proprietário:** aprova objetivos, risco aceite, recursos e prioridades.
- **Responsável do projeto:** mantém roadmap, dependências, decisões e evidências.
- **Responsável comercial:** analisa oportunidade, concorrência, fornecedor e estratégia de oferta.
- **Responsável financeiro:** valida custo total, impostos estimados com apoio especializado, capital de giro e margem.
- **Responsável por habilitação/conformidade:** confere documentos, exigências do edital e prazos.
- **Responsável técnico/logístico:** verifica conformidade do produto, disponibilidade, garantia, entrega e aceite.
- **Revisor independente:** participa quando o risco ou a segregação de funções exige.

Enquanto não houver nomeação formal, os papéis não devem ser atribuídos ficticiamente a pessoas específicas.

## 5. Gates mínimos

- **G0 — Entrada:** problema, beneficiário, proprietário, escopo e limites documentados.
- **G1 — Viabilidade:** evidência de demanda, fontes, alternativas, custo, margem, risco e dependências.
- **G2 — Desenho:** requisitos funcionais, arquitetura, dados, segurança, aceitação e plano de testes.
- **G3 — Construção validada:** revisão, testes proporcionais ao risco, rastreabilidade e documentação.
- **G4 — Prontidão operacional:** segurança, recuperação, monitorização, suporte, credenciais e rollback avaliados.
- **G5 — Operação/lançamento:** autorização explícita, checklist, acompanhamento e plano de reversão.
- **G6 — Encerramento:** aceite, pendências, arquivo/retenção, lições e aprovação de encerramento.

A preparação documental inicial não implica aprovação de qualquer gate além dos itens cuja evidência esteja registada.

## 6. Estados

Usar estados controlados: `PROPOSTO`, `EM_CURSO`, `BLOQUEADO`, `EM_REVISAO`, `APROVADO`, `REJEITADO`, `CONCLUIDO`, `DEPRECADO`. Para controlos monitorizados: `PASS`, `WARN`, `FAIL`, `UNKNOWN`. Ausência de dados nunca é PASS.

## 7. Segurança, privacidade e conformidade

Classificar dados e acessos antes de recolher ou armazenar. Utilizar fontes oficiais e respeitar termos de uso, limites de acesso e condições legais. Dados de pessoas, credenciais, propostas reservadas e informações comerciais não públicas não devem ser expostos no repositório público. Registar incidentes e exceções com responsável, risco, validade e ação de resolução.

## 8. Monitorização WATCHDOG

O projeto deverá declarar sistemas críticos, proprietário, criticidade, controlos, evidências, escalonamento e recuperação. A referência ao WATCHDOG da GOVERNANCA não prova monitorização ativa. Até integração, teste e aceite locais, o estado deve permanecer UNKNOWN ou EM_REVISAO.

## 9. Estado desta adoção

A adoção está **EM_REVISAO**. A presente constituição é um documento inicial de preparação; precisa de revisão formal, validação dos links e coerência com o padrão canónico. Não declarar conformidade integral apenas por criar os ficheiros.

## 10. Histórico

| Versão | Data | Alteração | Evidência |
|---|---|---|---|
| 0.1.0 | 2026-10-20 | Preparação inicial da governança local e gates | Branch de adoção |
