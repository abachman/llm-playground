# https://medium.com/@asvinjangid.kumar/creating-your-own-api-in-python-a-beginners-guide-59f4dd18d301

from flask import Flask, request, jsonify, make_response
from flask_cors import CORS  # The typical way to import flask-cors
from mlx_lm import load, generate

app = Flask(__name__)
CORS(app, resources=r"/chat")

model, tokenizer = load("mlx-community/Meta-Llama-3-8B-Instruct-4bit")


@app.before_request
def preflight():
    if request.method.lower() == "options":
        response = make_response()
        response.headers["Access-Control-Allow-Origin"] = request.headers.get("Origin")
        response.headers["Access-Control-Allow-Methods"] = "POST"
        response.headers["Access-Control-Allow-Headers"] = "content-type"
        return response


@app.route("/chat", methods=["POST", "OPTIONS"])
def chat():
    data = request.get_json()
    if "id" in data:
        message_id = data["id"]
    else:
        message_id = "0"

    messages = [
        {
            "role": "system",
            "content": "You are a friendly chatbot who has novel and interesting ideas about fashion. Keep your answers brief and encouraging.",
        },
        {"role": "user", "content": data["prompt"]},
    ]
    input_ids = tokenizer.apply_chat_template(messages, add_generation_prompt=True)
    prompt = tokenizer.decode(input_ids)
    response_content = generate(model, tokenizer, max_tokens=512, prompt=prompt)
    response = make_response(jsonify({"response": response_content, "id": message_id}))
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Methods"] = "POST"
    response.headers["Access-Control-Allow-Headers"] = "ContentType"
    return response


@app.route("/")
def hello():
    return jsonify({"message": "Hello, World!"})


if __name__ == "__main__":
    app.run(debug=True, port=5000)
