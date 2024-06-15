https://medium.com/@xuer.chen.human/beginners-guide-to-running-llama-3-8b-on-a-macbook-air-ffb380aeef0c

Setup:

```console
$ pyenv install 3.12.2
$ pip install mlx-lm torch
```

Get model from huggingface:

```console
$ pip install huggingface_hub hf_transfer
$ export HF_HUB_ENABLE_HF_TRANSFER=1
$ huggingface-cli download --local-dir Meta-Llama-3-8B-Instruct-4bit mlx-community/Meta-Llama-3-8B-Instruct-4bit
```

Simple hello world with prompt templating:

```python
from mlx_lm import load, generate

model, tokenizer = load("mlx-community/Meta-Llama-3-8B-Instruct-4bit")

question = "I'm a cool chap. Does a green shirt go with blue pants?"

messages = [ {"role": "system", "content": "You are a friendly chatbot."},
             {"role": "user", "content": question}, ]
input_ids = tokenizer.apply_chat_template(messages,
                                          add_generation_prompt=True)
prompt = tokenizer.decode(input_ids)
response = generate(model, tokenizer, prompt=prompt, verbose=True)
```

Based on: https://huggingface.co/meta-llama/Meta-Llama-3-8B-Instruct

