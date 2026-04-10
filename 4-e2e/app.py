import math

from flask import Flask, jsonify, request

app = Flask(__name__)

history = []


def _bad_request(message: str):
    return jsonify({"error": message}), 400


def _get_operands():
    data = request.get_json(silent=True)
    if not isinstance(data, dict):
        return None, None, _bad_request("invalid json")

    if "a" not in data:
        return None, None, _bad_request("missing field: a")
    if "b" not in data:
        return None, None, _bad_request("missing field: b")

    a = data.get("a")
    b = data.get("b")

    if isinstance(a, str) and not a.strip():
        return None, None, _bad_request("empty value: a")
    if isinstance(b, str) and not b.strip():
        return None, None, _bad_request("empty value: b")

    if isinstance(a, bool) or isinstance(b, bool):
        return None, None, _bad_request("invalid data type")
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        return None, None, _bad_request("invalid data type")

    if not math.isfinite(float(a)) or not math.isfinite(float(b)):
        return None, None, _bad_request("invalid number")

    max_abs = 10**12
    if abs(a) > max_abs or abs(b) > max_abs:
        return None, None, _bad_request("number too large")

    return a, b, None

@app.route("/")
def home():
    return "Welcome to the Flask APP."


@app.route("/health")
def health():
    return jsonify({"status": "ok"})


@app.route("/add", methods=["POST"])
def add():
    a, b, error = _get_operands()
    if error is not None:
        return error

    result = a + b
    history.append({"operation": "add", "a": a, "b": b, "result": result})
    return jsonify({"result": result})

@app.route("/subtract", methods=["POST"])
def subtract():
    a, b, error = _get_operands()
    if error is not None:
        return error

    result = a - b
    history.append({"operation": "subtract", "a": a, "b": b, "result": result})
    return jsonify({"result": result})


@app.route("/multiply", methods=["POST"])
def multiply():
    a, b, error = _get_operands()
    if error is not None:
        return error

    result = a * b
    history.append({"operation": "multiply", "a": a, "b": b, "result": result})
    return jsonify({"result": result})


@app.route("/divide", methods=["POST"])
def divide():
    a, b, error = _get_operands()
    if error is not None:
        return error

    if b == 0:
        return _bad_request("division by zero")

    try:
        result = a / b
    except ZeroDivisionError:
        return _bad_request("division by zero")

    history.append({"operation": "divide", "a": a, "b": b, "result": result})
    return jsonify({"result": result})

@app.route("/history", methods=["GET"])
def get_history():
    return jsonify(history), 200

if __name__ == "__main__":
    app.run(debug=True)
