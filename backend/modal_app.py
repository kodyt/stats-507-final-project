import modal

# ✅ 1. Define the Modal app correctly
app = modal.App("coding-tutor-api")

# ✅ 2. Define and attach the Docker image
image = (
    modal.Image.debian_slim()
    .pip_install(
        "flask", 
        "flask-cors", 
        "torch", 
        "transformers", 
        "accelerate", 
        "sentencepiece"
    )
)

# ✅ 3. Use modal.Function to wrap the Flask app as a WSGI (not ASGI) app
@app.function(image=image, min_containers=1, timeout=120)
@modal.wsgi_app()
def flask_app():
    from flask import Flask, request, jsonify
    from flask_cors import CORS
    from model.load_model import generate_full_explanation

    app = Flask(__name__)
    CORS(app)

    @app.route("/api/ask", methods=["POST"])
    def ask():
        data = request.get_json()
        code = data.get("code", "")
        question = data.get("question", "")
        answer = generate_full_explanation(code, question)
        return jsonify({"answer": answer})

    return app

if __name__ == "__main__":
    app.serve()