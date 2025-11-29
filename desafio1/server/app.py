from datetime import UTC, datetime
import socket

from flask import Flask, jsonify


app = Flask(__name__)


@app.route("/")
def index():
    return jsonify(
        {
            "message": "Servidor do Desafio 1 ativo",
            "hostname": socket.gethostname(),
            "timestamp": datetime.now(UTC).isoformat().replace("+00:00", "Z"),
        }
    )


if __name__ == "__main__":
    port = 8080
    app.run(host="0.0.0.0", port=port)
