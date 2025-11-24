from flask import Flask, jsonify

app = Flask(__name__)

USERS = [
    {"id": 1, "name": "Alice Costa", "email": "alice@example.com"},
    {"id": 2, "name": "Bruno Lima", "email": "bruno@example.com"},
    {"id": 3, "name": "Carla Mendes", "email": "carla@example.com"},
]


@app.route("/users")
def get_users():
    return jsonify(USERS)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=6001)
