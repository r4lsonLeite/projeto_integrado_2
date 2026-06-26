# Backend Flask MVC - Empreenda Mais Elas

O backend foi reorganizado para uma arquitetura MVC em Flask, separando responsabilidades em camadas de configuracao, modelos, repositorios, servicos, controllers e rotas de API. A nova base entrega autenticacao JWT, documentacao Swagger e uma estrutura orientada a objetos pronta para evoluir.

## O que foi feito

- Criada uma app factory em app/__init__.py.
- Centralizadas configuracoes em app/config.py.
- Inicializadas extensoes em app/extensions.py.
- Criados modelos de dominio em app/models.
- Criados repositorios baseados em SQLAlchemy em app/repositories.
- Implementadas regras de negocio em app/services.
- Criados controllers finos em app/controllers.
- Organizados endpoints por namespace em app/api/namespaces.
- Adicionada autenticacao JWT com login, registro e rota de perfil.
- Adicionada documentacao Swagger UI em /api/v1/docs.
- Adicionado seed inicial com uma usuaria administradora.
- Migradas as classes antigas da raiz para a estrutura nova em app/models.
- Removidos os arquivos legados de classes nao utilizados.
- Adicionado Flask-Migrate com migration inicial em migrations/versions.

## Estrutura da nova arquitetura

```text
projeto_integrado_2/
  app/
    api/
      namespaces/
    controllers/
    models/
    persistence_models.py
    repositories/
    routes/
    services/
    __init__.py
    config.py
    container.py
    extensions.py
  requirements.txt
  run.py
  migrations/
  README.md
  README_BACKEND.md
  empreenda_mais_elas.db
```

## Endpoints principais

- GET /api/v1/health
- POST /api/v1/auth/register
- POST /api/v1/auth/login
- GET /api/v1/auth/me
- GET /api/v1/usuarios
- GET /api/v1/usuarios/{id}
- GET /api/v1/produtos
- POST /api/v1/produtos
- GET /api/v1/pedidos
- POST /api/v1/pedidos
- GET /api/v1/mentorias
- POST /api/v1/mentorias
- GET /api/v1/trilhas
- POST /api/v1/trilhas
- GET /api/v1/anuncios
- POST /api/v1/anuncios
- GET /api/v1/mentorias-operacoes/agendas
- POST /api/v1/mentorias-operacoes/agendas
- GET /api/v1/mentorias-operacoes/avaliacoes
- POST /api/v1/mentorias-operacoes/avaliacoes
- GET /api/v1/parcerias/parceiros
- POST /api/v1/parcerias/parceiros
- GET /api/v1/parcerias/ofertas
- POST /api/v1/parcerias/ofertas
- GET /api/v1/financeiro/faturas
- POST /api/v1/financeiro/faturas
- GET /api/v1/financeiro/pagamentos
- POST /api/v1/financeiro/pagamentos
- GET /api/v1/suporte/enderecos
- POST /api/v1/suporte/enderecos
- GET /api/v1/suporte/metricas
- POST /api/v1/suporte/metricas
- GET /api/v1/suporte/notificacoes
- POST /api/v1/suporte/notificacoes
- GET /api/v1/aprendizagem/progressos
- POST /api/v1/aprendizagem/progressos
- GET /api/v1/aprendizagem/diagnosticos
- POST /api/v1/aprendizagem/diagnosticos

## Como executar

Instale as dependencias:

```bash
python -m pip install --user -r requirements.txt
```

Execute a aplicacao:

```bash
python run.py
```

O banco SQLite sera criado automaticamente no arquivo local abaixo:

```text
projeto_integrado_2/empreenda_mais_elas.db
```

Para aplicar migrations em um banco novo ou recriar o schema pelo fluxo do Alembic:

```bash
python -m flask --app run:app db upgrade -d migrations
```

Abra a documentacao:

```text
http://127.0.0.1:5000/api/v1/docs
```

## Fluxo de autenticacao

1. Cadastre uma usuaria em /api/v1/auth/register.
2. Faca login em /api/v1/auth/login.
3. Copie o token retornado.
4. Envie Authorization: Bearer <token> nas rotas protegidas.

## Usuario inicial

- E-mail: admin@empreendamaiselas.com
- Senha: admin123

## Observacoes importantes

- A persistencia atual usa SQLAlchemy sobre SQLite, com migration inicial versionada pelo Flask-Migrate.
- As classes antigas da raiz foram migradas para app/models e removidas da pasta principal.
- O fluxo de migrations pode usar AUTO_CREATE_DB=false quando voce quiser trabalhar apenas com Alembic sem bootstrap automatico.
- A estrutura atual ja permite separar melhor responsabilidades e testar cada camada isoladamente.