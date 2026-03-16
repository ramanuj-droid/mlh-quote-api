from flask import Flask, jsonify
import random
from quotes import quotes

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"message": "Welcome to the Quote API"})

@app.route("/quotes")
def get_quotes():
    return jsonify(quotes)

@app.route("/quotes/random")
def random_quote():
    return jsonify(random.choice(quotes))

@app.route("/quotes/<int:id>")
def get_quote(id):
    for q in quotes:
        if q["id"] == id:
            return jsonify(q)
    return jsonify({"error": "Quote not found"}), 404


if __name__ == "__main__":
    app.run(debug=True)