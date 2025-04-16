from flask import Flask, request, jsonify
from flask_cors import CORS
from model.load_model import generate_full_explanation

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return "🧠 AI Coding Tutor API is running!"

@app.route('/api/ask', methods=['POST'])
def ask():
    """
        Endpoint to handle code and question input and return the generated answer.
    """
    try:
        data = request.get_json()
        code = data.get('code', '')
        question = data.get('question', '')

        if not code or not question:
            return jsonify({'error': 'Missing code or question'}), 400

        answer = generate_full_explanation(code, question)
        return jsonify({'answer': answer})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/ping', methods=['GET'])
def ping():
    return jsonify({'status': 'ok'})

if __name__ == '__main__':
    app.run(port=8000, debug=True)