# Desafio 5 — Microsserviços com API Gateway

Arquitetura com três serviços Flask executando em containers Docker e orquestrados via docker-compose:

- **users_service** (`GET /users`): retorna usuários e seus dados de contato.
- **orders_service** (`GET /orders`): lista pedidos com status e usuário associado.
- **gateway** (`GET /users`, `GET /orders`): ponto único de entrada. Encaminha chamadas aos serviços internos usando variáveis `USERS_URL` e `ORDERS_URL`.

## Execução

```bash
docker compose up --build
```

Endpoints expostos pelo gateway em `http://localhost:7000`:

- `http://localhost:7000/users`
- `http://localhost:7000/orders`

Os serviços internos também ficam acessíveis diretamente (6001 e 6002), caso precise depurar.

## Arquitetura

```
           ┌──────────┐
           │ Gateway  │ 7000
           └───┬──────┘
               │
    ┌──────────┴──────────┐
    │                     │
┌──────────┐        ┌───────────┐
│ UsersSvc │ 6001   │ OrdersSvc │ 6002
└──────────┘        └───────────┘
```

## Boas práticas

- `depends_on` garante que o gateway só sobe após os serviços internos.
- Rede interna `desafio5-net` evita exposição desnecessária.
- Dockerfiles separados, facilitando deploy independente.

Para encerrar:
```bash
docker compose down
```
