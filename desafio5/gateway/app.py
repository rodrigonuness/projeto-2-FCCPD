import os

import requests
from flask import Flask, jsonify

USERS_URL = os.environ.get("USERS_URL", "http://users_service:6001/users")
ORDERS_URL = os.environ.get("ORDERS_URL", "http://orders_service:6002/orders")

app = Flask(__name__)


def proxy(url: str):
    response = requests.get(url, timeout=3)
    response.raise_for_status()
    return response.json()


@app.route("/users")
def gateway_users():
    return jsonify(proxy(USERS_URL))


@app.route("/orders")
def gateway_orders():
    return jsonify(proxy(ORDERS_URL))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7000)
