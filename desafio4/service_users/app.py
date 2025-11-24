from flask import Flask, jsonify

app = Flask(__name__)

USERS = [
    {"id": 1, "name": "Alice Costa", "active_since": "2023-01-10"},
    {"id": 2, "name": "Bruno Lima", "active_since": "2022-07-22"},
    {"id": 3, "name": "Carla Mendes", "active_since": "2021-05-03"},
]


@app.route("/users")
def list_users():
    return jsonify(USERS)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
