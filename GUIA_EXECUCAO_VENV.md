# Guia Completo: Executar Backend Flask no Ambiente Virtual

Este guia detalha como executar o projeto **Empreenda Mais Elas** em um ambiente Python isolado usando `venv`.

## Pré-requisitos

- Python 3.10+ instalado
- Git (opcional, para versionamento)
- Terminal/CMD com acesso ao interpretador Python

---

## 1. Criar e Ativar o Ambiente Virtual

### No Windows (PowerShell ou CMD)

```bash
# Navegar até a pasta do projeto
cd C:\Users\seu_usuario\Downloads\FACULDADE\POO\projetointegrado\projeto_integrado_2

# Criar o venv
python -m venv venv

# Ativar o venv
venv\Scripts\activate
```

Após ativar, você verá `(venv)` no início da linha do terminal:
```
(venv) C:\Users\seu_usuario\...\projeto_integrado_2>
```

### No Linux/macOS

```bash
cd ~/Downloads/FACULDADE/POO/projetointegrado/projeto_integrado_2
python3 -m venv venv
source venv/bin/activate
```

---

## 2. Instalar Dependências

Com o venv ativado, instale os pacotes necessários:

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

Isso instalará:
- Flask 3.1.1
- Flask-JWT-Extended 4.7.1
- flask-restx 1.3.0
- Flask-SQLAlchemy 3.1.1
- Flask-Migrate 4.0.7
- SQLAlchemy 2.0.41
- Werkzeug 3.1.3
- E dependências transitivases

---

## 3. Inicializar o Banco de Dados (Primeira Vez)

Se é a primeira vez executando o projeto, o banco SQLite será criado automaticamente. Você pode também usar Flask-Migrate manualmente:

```bash
# Aplicar migrations (cria o schema completo)
python -m flask --app run:app db upgrade -d migrations
```

Isso criará o arquivo `empreenda_mais_elas.db` com todas as tabelas.

---

## 4. Executar a Aplicação

Com as dependências instaladas e o banco pronto:

```bash
python run.py
```

Você verá uma saída como:

```
 * Serving Flask app 'app'
 * Debug mode: off
 * Running on http://127.0.0.1:5000/
Press CTRL+C to quit.
```

---

## 5. Acessar a Aplicação

### Documentação Swagger (UI interativa)
```
http://127.0.0.1:5000/api/v1/docs
```

Aqui você pode explorar todos os endpoints e testar requisições direto no navegador.

### Health Check (verificar se está rodando)
```
http://127.0.0.1:5000/api/v1/health
```

---

## 6. Exemplos de Fluxo Básico

### A. Registrar um novo usuário

**POST** `/api/v1/auth/register`

```json
{
  "nome": "Maria Silva",
  "email": "maria@empreendamaiselas.com",
  "senha": "senha_segura_123",
  "telefone": "11987654321",
  "endereco": "Rua das Flores, 123, São Paulo"
}
```

Resposta (sucesso):
```json
{
  "id": 1,
  "nome": "Maria Silva",
  "email": "maria@empreendamaiselas.com",
  "papel": "empreendedora"
}
```

### B. Fazer Login e Obter Token

**POST** `/api/v1/auth/login`

```json
{
  "email": "maria@empreendamaiselas.com",
  "senha": "senha_segura_123"
}
```

Resposta:
```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "usuario": {
    "id": 1,
    "nome": "Maria Silva",
    "email": "maria@empreendamaiselas.com"
  }
}
```

**Copie o `access_token` para usar em rotas protegidas.**

### C. Criar um Produto (requer autenticação)

**POST** `/api/v1/produtos`

Headers:
```
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
```

Body:
```json
{
  "usuario_id": 1,
  "titulo": "Curso de Marketing Digital",
  "descricao": "Aprenda as melhores técnicas de marketing para vender online",
  "valor": 99.90,
  "categoria": "educacao"
}
```

### D. Listar Todos os Produtos (sem autenticação)

**GET** `/api/v1/produtos`

---

## 7. Endpoints Principais

### Autenticação
- `POST /api/v1/auth/register` - Registrar novo usuário
- `POST /api/v1/auth/login` - Login e obter token JWT
- `GET /api/v1/auth/me` - Obter dados do usuário autenticado

### Marketplace
- `GET /api/v1/produtos` - Listar todos os produtos
- `POST /api/v1/produtos` - Criar novo produto (requer auth)
- `GET /api/v1/produtos/{id}` - Obter um produto
- `GET /api/v1/anuncios` - Listar anúncios
- `POST /api/v1/anuncios` - Criar anúncio (requer auth)
- `GET /api/v1/anuncios/{id}` - Obter um anúncio
- `PUT /api/v1/anuncios/{id}` - Atualizar anúncio (requer auth)
- `DELETE /api/v1/anuncios/{id}` - Deletar anúncio (requer auth)

### Mentorias
- `GET /api/v1/mentorias` - Listar mentorias
- `POST /api/v1/mentorias` - Agendar mentoria (requer auth)
- `GET /api/v1/mentorias-operacoes/agendas` - Listar agendas de mentoras
- `POST /api/v1/mentorias-operacoes/agendas` - Criar agenda (requer auth)

### Aprendizagem
- `GET /api/v1/trilhas` - Listar trilhas de aprendizado
- `POST /api/v1/trilhas` - Criar trilha (requer auth)
- `GET /api/v1/aprendizagem/progressos` - Listar progresso de conteúdos
- `POST /api/v1/aprendizagem/progressos` - Registrar progresso (requer auth)

### Parcerias
- `GET /api/v1/parcerias/parceiros` - Listar parceiros
- `POST /api/v1/parcerias/parceiros` - Criar parceiro (requer auth)
- `GET /api/v1/parcerias/parceiros/{id}` - Obter parceiro
- `PUT /api/v1/parcerias/parceiros/{id}` - Atualizar parceiro (requer auth)
- `DELETE /api/v1/parcerias/parceiros/{id}` - Deletar parceiro (requer auth)

### Financeiro
- `GET /api/v1/financeiro/faturas` - Listar faturas
- `POST /api/v1/financeiro/faturas` - Criar fatura (requer auth)
- `GET /api/v1/financeiro/pagamentos` - Listar pagamentos
- `POST /api/v1/financeiro/pagamentos` - Registrar pagamento (requer auth)

### Suporte
- `GET /api/v1/suporte/enderecos` - Listar endereços
- `POST /api/v1/suporte/enderecos` - Adicionar endereço (requer auth)
- `GET /api/v1/suporte/notificacoes` - Listar notificações
- `POST /api/v1/suporte/notificacoes` - Criar notificação (requer auth)

---

## 8. Testar com cURL (exemplo)

Se preferir usar a linha de comando:

```bash
# Health check
curl http://127.0.0.1:5000/api/v1/health

# Registrar usuário
curl -X POST http://127.0.0.1:5000/api/v1/auth/register \
  -H "Content-Type: application/json" \
  -d '{"nome":"Teste","email":"teste@email.com","senha":"123456"}'

# Login
curl -X POST http://127.0.0.1:5000/api/v1/auth/login \
  -H "Content-Type: application/json" \
  -d '{"email":"teste@email.com","senha":"123456"}'

# Criar produto (copie o token do login acima)
curl -X POST http://127.0.0.1:5000/api/v1/produtos \
  -H "Authorization: Bearer SEU_TOKEN_AQUI" \
  -H "Content-Type: application/json" \
  -d '{"usuario_id":1,"titulo":"Produto","descricao":"Desc","valor":50,"categoria":"teste"}'
```

---

## 9. Trabalhar com Git no venv

Se quiser commitar as mudanças sem incluir o venv:

```bash
# Verificar se .gitignore já existe
cat .gitignore

# Se não existir, criar um
echo "venv/" >> .gitignore
echo "__pycache__/" >> .gitignore
echo "*.pyc" >> .gitignore
echo "empreenda_mais_elas.db" >> .gitignore
echo ".env" >> .gitignore

# Commitar
git add .
git commit -m "Backend com SQLAlchemy e endpoints novos"
git push
```

---

## 10. Desativar o Ambiente Virtual

Quando terminar:

```bash
# Windows, Linux ou macOS
deactivate
```

---

## 11. Dicas e Troubleshooting

### "command not found: python"
Use `python3` em vez de `python` no Linux/macOS.

### "ModuleNotFoundError" ao executar
Certifique-se de que:
1. O venv está **ativado** (você vê `(venv)` no terminal)
2. Você rodou `pip install -r requirements.txt` dentro do venv

### Banco de dados corrompido
Deletar o arquivo e deixar recriar:
```bash
rm empreenda_mais_elas.db
python run.py
```

### Tentar rodar migrations sem venv ativado
```bash
# Ativar venv primeiro
venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/macOS

# Depois rodar
python -m flask --app run:app db upgrade -d migrations
```

### Porta 5000 já em uso
```bash
# Mudar porta no run.py
app.run(debug=False, port=5001)
```

---

## 12. Estrutura do Projeto

```
projeto_integrado_2/
├── app/
│   ├── api/
│   │   ├── namespaces/          # Endpoints organizados por contexto
│   │   └── __init__.py
│   ├── controllers/             # Lógica das rotas
│   ├── models/                  # Classes de domínio (não ORM)
│   ├── repositories/            # Acesso aos dados (SQLAlchemy)
│   ├── services/                # Regras de negócio
│   ├── persistence_models.py    # Modelos SQLAlchemy (ORM)
│   ├── config.py                # Configurações
│   ├── container.py             # Injeção de dependência
│   ├── extensions.py            # Extensões Flask
│   └── __init__.py              # App factory
├── migrations/                  # Versionamento do banco (Alembic)
├── venv/                        # Ambiente virtual (não commitir)
├── requirements.txt             # Dependências
├── run.py                       # Script de entrada
├── test_ep1.py                  # Testes do domínio
└── empreenda_mais_elas.db      # Banco de dados SQLite
```

---

## Próximas Etapas

1. Adicionar testes automatizados com `pytest`
2. Configurar variáveis de ambiente com `.env`
3. Adicionar autenticação por papel (RBAC)
4. Integrar com frontend em React
5. Deploy em produção (Heroku, AWS, etc)

---

**Desenvolvido com Python 3.12 e Flask 3.1.1**
