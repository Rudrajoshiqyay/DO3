from flask import Flask, jsonify
import math

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, World!"

@app.route('/square/<int:number>')
def square(number):
    return jsonify({"number": number, "square": number * number})

@app.route('/factorial/<int:number>')
def factorial(number):
    if number < 0:
        return jsonify({"error": "Number must be non-negative"}), 400
    result = math.factorial(number)
    return jsonify({"number": number, "factorial": result})

@app.route('/health')
def health():
    return jsonify({"status": "healthy"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
