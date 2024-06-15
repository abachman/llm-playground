from mlx_lm import load, generate

model, tokenizer = load("mlx-community/Meta-Llama-3-8B-Instruct-4bit")

question = "I'm a cool chap. Does a green shirt go with blue pants?"

messages = [ {"role": "system", "content": "You are a friendly chatbot who has novel and interesting ideas about fashion. Keep your answers brief and encouraging."},
             {"role": "user", "content": question}, ]
input_ids = tokenizer.apply_chat_template(messages,
                                          add_generation_prompt=True)
prompt = tokenizer.decode(input_ids)
response = generate(model,
                    tokenizer,
                    max_tokens=256,
                    prompt=prompt,
                    verbose=True)

print(response)