from flask import Flask, jsonify

app = Flask(__name__)

ORDERS = [
    {"id": 101, "user_id": 1, "total": 199.90, "status": "shipped"},
    {"id": 102, "user_id": 2, "total": 89.50, "status": "processing"},
    {"id": 103, "user_id": 1, "total": 15.00, "status": "delivered"},
]


@app.route("/orders")
def get_orders():
    return jsonify(ORDERS)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=6002)
