# Desafio 2 — Volumes e Persistência

Este desafio mostra como manter os dados mesmo após remover os containers usando volumes Docker nomeados. Aqui utilizamos um banco SQLite simples gravado no volume `desafio2-data`.

## Serviços

- **seed**: cria o banco `desafio2.db`, garante a tabela `users` e insere dados de exemplo.
- **reader**: abre o mesmo arquivo SQLite e imprime os registros encontrados para demonstrar a persistência.

Ambos apontam para `/data/desafio2.db`, montado a partir do volume.

## Como executar

1. Subir os serviços:
   ```bash
   docker compose up --build
   ```
   O `seed` roda uma vez e finaliza; o `reader` continua em execução mostrando os usuários.
2. Encerrar os containers:
   ```bash
   docker compose down
   ```
3. (Prova de persistência) Subir apenas o `reader` novamente, sem recriar o volume:
   ```bash
   docker compose up reader
   ```
   Ele mostrará os mesmos registros, comprovando que o volume `desafio2-data` manteve o arquivo SQLite.
4. Para remover os dados definitivamente: `docker volume rm desafio2-data`.

## Estrutura

```
seed/
  Dockerfile
  app.py
reader/
  Dockerfile
  app.py
```

Cada serviço é encapsulado em seu container, mas compartilham o volume declarado no `docker-compose.yml`.
