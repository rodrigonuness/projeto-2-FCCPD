import os
from datetime import UTC, datetime

import psycopg2
import redis
from flask import Flask, jsonify

app = Flask(__name__)

DB_CONFIG = {
    "dbname": os.environ.get("POSTGRES_DB", "appdb"),
    "user": os.environ.get("POSTGRES_USER", "appuser"),
    "password": os.environ.get("POSTGRES_PASSWORD", "apppass"),
    "host": os.environ.get("POSTGRES_HOST", "db"),
    "port": int(os.environ.get("POSTGRES_PORT", "5432")),
}
REDIS_HOST = os.environ.get("REDIS_HOST", "cache")
REDIS_PORT = int(os.environ.get("REDIS_PORT", "6379"))


@app.route("/")
def healthcheck():
    status = {
        "timestamp": datetime.now(UTC).isoformat().replace("+00:00", "Z"),
        "postgres": check_postgres(),
        "redis": check_redis(),
    }
    return jsonify(status)


def check_postgres():
    try:
        with psycopg2.connect(**DB_CONFIG) as conn:
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


def check_redis():
    try:
        client = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)
        client.incr("hits")
        total = client.get("hits")
        return {"ok": True, "count": total}
    except Exception as exc:  # noqa: BLE001
        return {"ok": False, "error": str(exc)}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
