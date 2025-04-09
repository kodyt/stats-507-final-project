from flask import Flask, request, jsonify
from model.load_model import get_explanation
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "http://localhost:5173"}})

@app.route('/api/ask', methods=['POST'])
def ask():
    # code = request.json.get('code', '')
    # explanation = get_explanation(code)
    # return jsonify({"explanation": explanation})
    
    data = request.get_json()
    code = data.get('code')
    question = data.get('question')

    # Placeholder logic
    answer = f"Got your question: '{question}' about this code:\n{code}"
    return jsonify({'answer': answer})

if __name__ == '__main__':
    app.run(port=5000, debug=True)