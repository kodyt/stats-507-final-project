from flask import Flask, request, jsonify
from model.load_model import get_explanation

app = Flask(__name__)

@app.route('/explain', methods=['POST'])
def explain():
    code = request.json.get('code', '')
    explanation = get_explanation(code)
    return jsonify({"explanation": explanation})

if __name__ == '__main__':
    app.run(port=5000)