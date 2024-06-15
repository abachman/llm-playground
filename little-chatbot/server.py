# https://medium.com/@asvinjangid.kumar/creating-your-own-api-in-python-a-beginners-guide-59f4dd18d301

from flask import Flask, request, jsonify
from mlx_lm import load, generate

app = Flask(__name__)

model, tokenizer = load("mlx-community/Meta-Llama-3-8B-Instruct-4bit")


@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    messages = [
        {"role": "system", "content": "You are a friendly chatbot who has novel and interesting ideas about fashion. Keep your answers brief and encouraging."},
        {"role": "user", "content": data["prompt"]},
    ]
    input_ids = tokenizer.apply_chat_template(messages, add_generation_prompt=True)
    prompt = tokenizer.decode(input_ids)
    response = generate(model, tokenizer, max_tokens=512, prompt=prompt)
    return jsonify({"response": response})


@app.route("/")
def hello():
    return jsonify({ 'message': "Hello, World!" })


if __name__ == "__main__":
    app.run(debug=True, port=5000)
