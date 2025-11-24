import os
from datetime import UTC, datetime

import requests
from flask import Flask, jsonify

SERVICE_USERS_URL = os.environ.get("SERVICE_USERS_URL", "http://service_users:5001/users")
app = Flask(__name__)


def fetch_users():
    response = requests.get(SERVICE_USERS_URL, timeout=3)
    response.raise_for_status()
    return response.json()


@app.route("/reports")
def generate_report():
    users = fetch_users()
    enriched = [
        {
            "user": user["name"],
            "since": user["active_since"],
            "message": f"Usuário {user['name']} ativo desde {user['active_since']}",
        }
        for user in users
    ]
    return jsonify(
        {
            "generated_at": datetime.now(UTC).isoformat().replace("+00:00", "Z"),
            "total": len(enriched),
            "data": enriched,
        }
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)
