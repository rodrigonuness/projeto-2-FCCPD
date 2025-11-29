# Desafio 3 — Docker Compose Orquestrando Serviços

Aplicação Flask que depende de PostgreSQL e Redis. O objetivo é demonstrar a orquestração de três serviços via Docker Compose.

## Arquitetura

- **db** (PostgreSQL): persiste as solicitações (tabela `hits`).
- **cache** (Redis): contador rápido de acessos.
- **web** (Flask): endpoint `/` que registra um hit no Postgres e incrementa o contador no Redis.

```
        ┌────────┐
        │  web   │
        └───┬────┘
            │
   ┌────────┴────────┐
   │                 │
┌──────────┐       ┌────────┐
│ Postgres │       │ Redis  │
└──────────┘       └────────┘
```

## Execução

1. Na pasta `desafio3`, rode:
   ```bash
   docker compose up --build
   ```
2. Acesse `http://localhost:5000/` para verificar o JSON com os status dos serviços e contadores.
3. Logs dos serviços:
   ```bash
   docker compose logs -f web
   ```
4. Encerrar tudo:
   ```bash
   docker compose down
   ```

## Observação:
Professor, as vezes a porta 5000 pode estar ocupada pelo próprio docker, pode-se mudar a porta de 5000 para alguma outra (como 5003, por exemplo) se necessário.


## Boas práticas aplicadas
- Uso de `depends_on` e rede interna `desafio3-net`.
- Variáveis de ambiente definidas no `docker-compose.yml`.
- Volumes nomeados para dados do Postgres (`desafio3-pgdata`).
