# Relatório de Entrega - Engenharia de Software

## Projeto


Empreenda Mais Elas - Plataforma de Apoio ao Empreendedorismo Feminino


## Disciplina

Engenharia de Software (Projeto Integrado III)


## Integrantes

- Marcos Felipe Ferreira Duarte (Matrícula: 2025014117)
- José Junio de Souza Matias (Matrícula: 2025014028)
- José Railson Leite da Silva (Matrícula: 2025019392)

## Professor


Luís Fabrício de Freitas Souza


## Tipo de Entrega (2 arquivos)

Conforme orientação da atividade, esta entrega é composta por exatamente 2 arquivos:
1

1. Relatório de Entrega

- Arquivo: RELATORIO_ENTREGA.md (este arquivo)
- Conteúdo: síntese do trabalho, atendimento aos critérios, evidências e link do repositório


1. Documentação Arquitetural

- Arquivo: ARQUITETURA.md
- Conteúdo: modelo arquitetural, decisões técnicas, padrões, boas práticas, diagramas e evolução

## Repositório GitHub do Projeto



- Link do repositório: inserir-link-aqui

Observação: o link do repositório deve ser informado no relatório final da equipe para conferência da banca.

## Atendimento aos Critérios Avaliativos


### 1) Clareza e consistência do modelo arquitetural (0-2,0)


Evidências no arquivo ARQUITETURA.md:

- Visão geral do sistema, problema e objetivo do MVP
- Estrutura em camadas com responsabilidades claras

- Componentes principais mapeados por domínio

- Fluxos de integração entre frontend, backend e banco

### 2) Qualidade das justificativas técnicas (0-2,0)

Evidências no arquivo ARQUITETURA.md:



- Decisões técnicas documentadas com impactos positivos e trade-offs
- Justificativas para stack escolhida (React, Flask, SQLAlchemy, JWT)
- Relação entre escolha tecnológica e metas do MVP

### 3) Uso adequado de padrões arquiteturais e boas práticas (0-2,0)



Evidências no arquivo ARQUITETURA.md:

- Padrões: MVC, REST, SPA, Cliente-Servidor e Arquitetura em Camadas
- Boas práticas: separação de responsabilidades, componentização, validação e segurança
- Organização por módulos e serviços


### 4) Clareza e profundidade das explicações no README (0-2,0)

Evidências nos READMEs do projeto:

- Explicação da arquitetura em linguagem própria da equipe

- Instruções de execução e organização dos módulos
- Contexto do problema, solução e impacto

### 5) Organização, documentação e qualidade do repositório GitHub (0-2,0)

Evidências no repositório:



- Estrutura de pastas separando frontend e backend
- Documentação centralizada e navegável
- Arquivos de apoio para execução e entendimento

## Resumo Técnico da Solução

- Frontend SPA em React com rotas protegidas e integração com API
- Backend Flask com autenticação JWT e endpoints REST
- Persistência via SQLAlchemy com suporte a SQLite e PostgreSQL
- Fluxos principais integrados: autenticação, produtos, mentorias, trilhas e diagnóstico

## Checklist Final da Entrega

- [x] Arquivo 1: RELATORIO_ENTREGA.md
- [x] Arquivo 2: ARQUITETURA.md
- [ ] Link do GitHub preenchido no relatório
- [ ] Nomes dos integrantes preenchidos

---

## EP3 - MVP Web Funcional - Complementação

Este relatório também cobre a **Entrega Parcial 3 (EP3)**, que exige a demonstração de um MVP funcional com documentação de processo de desenvolvimento.

### Itens de EP3 Atendidos

#### 1. Desenvolvimento do MVP Web ✅

**Interface Web funcional:**
- Frontend em React com navegação entre principais telas
- Componentes reutilizáveis (Navbar, Footer, Forms, Cards)
- Rotas protegidas com ProtectedRoute.jsx
- Responsividade mobile-first com Tailwind CSS

**Funcionalidades essenciais implementadas:**
- Autenticação (Registro, Login, Logout)
- Gestão de Usuárias (Perfil, Dados)
- Marketplace (Listagem, Filtro, Carrinho)
- Mentorias (Agendamento, Avaliação)
- Trilhas de Aprendizagem (Visualização, Progresso)
- Diagnóstico Inicial (Questionário dinâmico)
- Painel Administrativo (Métricas e Monitoramento)

**Integração entre componentes:**
- Frontend integrado com API Backend via Fetch + JWT
- Proxy Vite para resolução de CORS
- Adaptadores para normalização de dados
- Fluxo completo: Login → Dashboard → Módulos → Dados em tempo real

**Organização do projeto:**
- Estrutura clara: `/empreendamaiselas` (frontend) e `/projeto_integrado_2` (backend)
- Padrão de pastas: components, pages, services, layouts
- Convenção de nomenclatura consistente
- Documentação centralizada

#### 2. Organização do Projeto GitHub ✅

**Código-fonte completo:**
- Frontend React com Vite em `empreendamaiselas/`
- Backend Flask com SQLAlchemy em `projeto_integrado_2/`
- Todos os modelos, controllers, services e componentes

**Estrutura de pastas adequada:**
```
├── empreendamaiselas/
│   ├── src/
│   │   ├── components/      # Componentes reutilizáveis
│   │   ├── pages/          # Páginas/Rotas
│   │   ├── services/       # Integração com API
│   │   └── layouts/        # Layouts compartilhados
│   └── package.json
│
└── projeto_integrado_2/
    ├── app/
    │   ├── models/         # Modelos de dados
    │   ├── api/            # Controllers REST
    │   └── services/       # Lógica de negócio
    ├── run.py
    └── requirements.txt
```

**Histórico de commits:**
- Commits representando evolução (setup, features, integração, docs)
- Mensagens descritivas indicando mudanças
- Ramificação organizada (main + feature branches)

**Documentação suficiente:**
- README.md completo em ambos os subprojetos
- ARQUITETURA.md com decisões e padrões
- RELATORIO_ENTREGA.md com síntese geral
- Instruções de setup e execução

#### 3. Documentação do Projeto (README) ✅

**a) Descrição do Projeto**
- Objetivo: Plataforma de inclusão digital e apoio ao empreendedorismo feminino
- Problema: Barreiras de entrada no mercado para mulheres micro-empreendedoras
- Público-alvo: Mulheres em fase de ideia ou com negócio ativo, mentoras, administradoras
- Principais funcionalidades: Autenticação, Marketplace, Mentorias, Trilhas, Diagnóstico, Admin

**b) Tecnologias Utilizadas**
- Frontend: React 19.2.6, Vite 8.0.12, React Router 7.1.1, Tailwind CSS 3.4.19, Fetch API
- Backend: Python 3.10+, Flask 2.x, Flask-RESTx 0.5.x, SQLAlchemy 2.0+, JWT
- Banco: SQLite (dev), PostgreSQL (produção)
- Ferramentas: GitHub, VS Code, Discord

**c) Estrutura do Projeto**
- Documentação clara com árvore de diretórios
- Explicação de responsabilidades de cada pasta
- Padrão MVC com separação clara de camadas

**d) Instalação e Execução**
- Passo a passo para clonar repositório
- Instalação de dependências (npm para frontend, pip para backend)
- Configuração de ambiente
- Execução de ambos os servidores
- Acesso ao sistema (URLs e credenciais de teste)

**e) Processo de Desenvolvimento**
- Divisão de tarefas em 4 fases (Planejamento, Backend, Frontend, Testes)
- Uso do GitHub com commits e branches
- Estratégia de versionamento clara
- Dificuldades encontradas (CORS, JWT, normalização) com soluções adotadas
- Status atual (concluído vs. em evolução)

#### 4. Demonstração do MVP ✅

**Telas e Funcionalidades Demonstradas:**
- Login/Registro com autenticação JWT
- Dashboard personalizado com métricas
- Marketplace com produtos reais
- Agendamento de mentorias
- Trilhas de aprendizagem com conteúdo
- Diagnóstico dinâmico inicial
- Painel administrativo com relatórios

**Fluxos de Navegação:**
- Usuária anônima → Registro → Login → Dashboard
- Dashboard → Marketplace → Carrinho → Pedido
- Dashboard → Mentorias → Agendamento → Avaliação
- Dashboard → Trilhas → Conteúdo → Progresso
- Admin → Painel → Métricas → Relatórios

**Exemplos de Utilização:**
- Caso de uso 1: Nova empreendedora cadastra, faz diagnóstico, recebe trilha personalizada
- Caso de uso 2: Empreendedora com negócio ativo publica produto no marketplace
- Caso de uso 3: Administrador monitora impacto e engajamento em tempo real

**Evidências de Funcionamento:**
- Backend responde com código 200/201 para requisições bem-sucedidas
- Endpoints REST funcionais: /auth/register, /auth/login, /produtos, /mentorias, /trilhas, /pedidos
- Persistência de dados: Dados armazenados no banco e recuperáveis
- Autenticação: Token JWT gerado e validado em cada requisição

---

## Observação Final

Para envio no ambiente da disciplina, esta entrega contém as documentações e evidências de:

**Entrega Parcial 2 (EP2) - Arquitetura de Software:**
- RELATORIO_ENTREGA.md
- ARQUITETURA.md

**Entrega Parcial 3 (EP3) - MVP Web Funcional:**
- empreendamaiselas/README.md (com seções: Descrição, Tecnologias, Estrutura, Instalação, Processo de Desenvolvimento, Demonstração)
- projeto_integrado_2/README.md (com informações do backend)
- Repositório GitHub com código-fonte completo
- Histórico de commits e organização do projeto
- MVP funcional rodando em http://127.0.0.1:5173 (frontend) e http://127.0.0.1:7000 (backend)
