from flask import Flask, request, jsonify
from model.load_model import get_explanation
from flask_cors import CORS


app = Flask(__name__)
CORS(app, origins='*')

@app.route('/')
def index():
    return "Welcome to the code explanation API!"

@app.route('/api/ask', methods=['POST'])
def ask():
    # code = request.json.get('code', '')
    # explanation = get_explanation(code)
    # return jsonify({"explanation": explanation})
    
    data = request.get_json()
    code = data.get('code')
    question = data.get('question')

    response = get_explanation(code)
    print(response)
    # Placeholder logic
    answer = f"Got your question: '{question}' about this code:\n{code}"
    return jsonify({'answer': answer})

@app.route('/api/users', methods=['GET'])
def users():
    return jsonify({"users": ["Alice", "Bob", "Charlie"]})

if __name__ == '__main__':
    app.run(port=8000, debug=True)


# def factorial(n):
#     """
#     Calculate the factorial of a number.
    
#     :param n: Non-negative integer
#     :return: Factorial of n
#     """
#     if n < 0:
#         raise ValueError("Factorial is not defined for negative numbers")
#     if n == 0 or n == 1:
#         return 1
#     return n * factorial(n - 1)