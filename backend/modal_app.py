import modal

# Create the Modal app
app = modal.App("coding-tutor-api")

# Define the image for the container
image = modal.Image.debian_slim().pip_install(
    "flask", "flask-cors", "torch", "transformers", "accelerate", "sentencepiece"
)

# The actual Flask app wrapped in Modal
@modal.function(image=image, keep_warm=1, timeout=60)
@modal.asgi_app()
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
