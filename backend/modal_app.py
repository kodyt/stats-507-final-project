import modal

app = modal.App("tinyllama-coding-tutor")

image = (
    modal.Image.from_registry("nvidia/cuda:12.1.1-base-ubuntu22.04", add_python="3.10")
    .apt_install("git")
    .pip_install(
        "flask", "flask-cors", "torch", "transformers", "accelerate", "sentencepiece"
    )
)

@app.function(image=image, gpu="A10G", timeout=300, keep_warm=1)
@modal.wsgi_app()
def flask_app():
    from flask import Flask, request, jsonify
    from flask_cors import CORS
    from model.load_model import generate_full_explanation

    web_app = Flask(__name__)
    CORS(web_app)

    @web_app.route("/api/ask", methods=["POST"])
    def ask():
        data = request.get_json()
        code = data.get("code", "")
        question = data.get("question", "")
        answer = generate_full_explanation(code, question)
        return jsonify({"answer": answer})

    return web_app
