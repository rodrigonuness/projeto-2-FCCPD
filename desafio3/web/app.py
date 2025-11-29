import os
from datetime import UTC, datetime

import psycopg2
import redis
from flask import Flask, jsonify

app = Flask(__name__)

CONFIG_BD = {
    "dbname": os.environ.get("POSTGRES_DB", "appdb"),
    "user": os.environ.get("POSTGRES_USER", "appuser"),
    "password": os.environ.get("POSTGRES_PASSWORD", "apppass"),
    "host": os.environ.get("POSTGRES_HOST", "db"),
    "port": int(os.environ.get("POSTGRES_PORT", "5432")),
}
HOST_REDIS = os.environ.get("REDIS_HOST", "cache")
PORTA_REDIS = int(os.environ.get("REDIS_PORT", "6379"))


@app.route("/")
def verificar_saude():
    status = {
        "timestamp": datetime.now(UTC).isoformat().replace("+00:00", "Z"),
        "postgres": verificar_postgres(),
        "redis": verificar_redis(),
    }
    return jsonify(status)


def verificar_postgres():
    try:
        with psycopg2.connect(**CONFIG_BD) as conn:
            with conn.cursor() as cur:
                cur.execute(
                    "CREATE TABLE IF NOT EXISTS hits (id SERIAL PRIMARY KEY, created_at TIMESTAMP NOT NULL)"
                )
                cur.execute("INSERT INTO hits (created_at) VALUES (NOW()) RETURNING id")
                last_id = cur.fetchone()[0]
                cur.execute("SELECT COUNT(*) FROM hits")
                total_hits = cur.fetchone()[0]
        return {"ok": True, "last_hit_id": last_id, "total_hits": total_hits}
    except Exception as exc:  # noqa: BLE001
        return {"ok": False, "error": str(exc)}


def verificar_redis():
    try:
        client = redis.Redis(host=HOST_REDIS, port=PORTA_REDIS, decode_responses=True)
        client.incr("hits")
        total = client.get("hits")
        return {"ok": True, "count": total}
    except Exception as exc:  # noqa: BLE001
        return {"ok": False, "error": str(exc)}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
