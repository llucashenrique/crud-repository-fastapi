# CRUD Customers — FastAPI + PostgreSQL + Streamlit (Docker Compose)

## Visão geral

Este projeto implementa um **CRUD completo de clientes** com:

- **Backend**: FastAPI (Python) + SQLAlchemy (ORM)
- **Banco de dados**: PostgreSQL (Docker)
- **Frontend**: Streamlit (Python) consumindo a API via HTTP
- **Orquestração**: Docker Compose

O objetivo é disponibilizar:

- **API REST** com endpoints para criar, listar, atualizar e remover clientes
- **Interface Web (Streamlit)** para operar o CRUD visualmente

---

## Funcionalidades

### Backend (FastAPI)
- `POST /customers` — criar cliente
- `GET /customers` — listar clientes
- `GET /customers/{id}` — buscar cliente por ID
- `PUT /customers/{id}` — atualizar cliente
- `DELETE /customers/{id}` — remover cliente

### Frontend (Streamlit)
- Listagem de clientes em tabela
- Formulário para criação de cliente
- Seleção por ID para editar/deletar

---

## Estrutura do projeto

```bash
crud-postgres-fastapi/
├── Dockerfile                 # Dockerfile do backend (FastAPI)
├── docker-compose.yml         # Orquestra API + DB + Frontend
├── requirements.txt           # Dependências do backend
├── .env                       # Variáveis do Postgres (credenciais)
├── app/
│   ├── main.py
│   ├── db.py
│   ├── models.py
│   ├── schemas.py
│   ├── crud.py
│   └── routers/
│       └── customers.py
└── frontend/
    ├── Dockerfile             # Dockerfile do frontend (Streamlit)
    ├── requirements.txt       # Dependências do frontend
    └── streamlit_app.py
```

##  Pré-requisitos

- Docker Engine  
- Docker Compose (plugin v2)

Verifique se estão instalados:

```bash
docker --version
docker compose version
```

## Variáveis de ambiente

```bash
POSTGRES_USER=crud_user
POSTGRES_PASSWORD=crud_pass
POSTGRES_DB=crud_db
```

## Como executar (Docker Compose)

```bash
docker compose up -d --build

docker ps
```
## Como acessar?

- **FastAPI (Swagger UI):** [Abrir documentação](http://localhost:8000/docs)
- **Streamlit (Frontend):** [Abrir aplicação](http://localhost:8501)

## Testes rápidos (via curl)

- Criar cliente
```bash
curl -X POST "http://localhost:8000/customers" \
  -H "Content-Type: application/json" \
  -d '{"name":"Lucas","email":"lucas@email.com"}'
```

- Listar clientes
```bash
curl -X POST "http://localhost:8000/customers" \
  -H "Content-Type: application/json" \
  -d '{"name":"Lucas","email":"lucas@email.com"}'
```

- Buscar por ID
```bash
curl -X POST "http://localhost:8000/customers" \
  -H "Content-Type: application/json" \
  -d '{"name":"Lucas","email":"lucas@email.com"}'
```

- Atualizar cliente
```bash
curl -X PUT "http://localhost:8000/customers/1" \
  -H "Content-Type: application/json" \
  -d '{"name":"Lucas Henrique"}'
```

- Deletar cliente
```bash
curl -X DELETE "http://localhost:8000/customers/1"
```

## Como entrar no banco
```bash
docker exec -it postgres_crud bash
psql -U crud_user -d crud_db
\dt
SELECT * FROM customers;
```

## Parar os serviços
```bash
docker compose down
```