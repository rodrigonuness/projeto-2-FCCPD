# Desafio 4 — Microsserviços Independentes

Dois microsserviços Flask comunicam-se via HTTP sem gateway intermediário.

## Serviços

- **service_users** (`GET /users`): retorna lista JSON de usuários ativos e respectivas datas.
- **service_reports** (`GET /reports`): consome `service_users`, enriquece os dados e devolve frases formatadas.

Ambos possuem Dockerfiles próprios e são orquestrados por um `docker-compose.yml` simples.

## Execução

```bash
docker compose up --build
```

Endpoints:

- `http://localhost:5001/users`
- `http://localhost:5002/reports`

O service_reports usa a variável `SERVICE_USERS_URL` para localizar o outro serviço.

## Estrutura

```
service_users/
  Dockerfile
  app.py
  requirements.txt
service_reports/
  Dockerfile
  app.py
  requirements.txt
docker-compose.yml
```

Cada serviço é independente, permitindo testes e deploys separados, mas compartilham a mesma rede Docker (`desafio4-net`).
