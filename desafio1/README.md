# Desafio 1 — Containers em Rede

Este desafio demonstra dois containers conectados por uma rede Docker customizada. O servidor Flask responde na porta 8080 e o cliente executa requisições HTTP periódicas e imprime os resultados no log.

## Arquitetura

- **server**: aplicação Flask expondo `GET /` com informações do host.
- **client**: script Python com `requests` que chama o servidor a cada 5 segundos e registra o retorno.
- **Rede**: rede Docker nomeada `desafio1-net`, compartilhada pelos dois containers.

```
client ----HTTP---> server (porta 8080)
   ^                         |
   |_____ rede desafio1-net__|
```

## Como executar

1. Na pasta `desafio1`, construa e suba os serviços:
   ```bash
   docker compose up --build
   ```
2. Aguarde o log do `client` mostrar respostas `OK`. O servidor fica exposto em `http://localhost:8080` para testes manuais.
3. Para ver apenas os logs do cliente:
   ```bash
   docker compose logs -f client
   ```
4. Encerrar e remover containers mantendo a rede:
   ```bash
   docker compose down
   ```

## Demonstração dos logs

Exemplo de saída (truncado):
```
client  | [2025-11-24T17:40:00.123456Z] OK: {"message": "Servidor do Desafio 1 ativo", ...}
```
Isso comprova a comunicação contínua entre os containers.
