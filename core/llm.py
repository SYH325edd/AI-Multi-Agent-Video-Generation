import requests

API_KEY = "ark-7cfb3a97-7bac-406a-a775-142c1b29ea91-4f2a1"
URL = "https://ark.cn-beijing.volces.com/api/v3/chat/completions"

def call_llm(system_prompt: str, user_input: str, model: str):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": model,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_input}
        ]
    }

    res = requests.post(URL, json=payload, headers=headers)
    return res.json()
