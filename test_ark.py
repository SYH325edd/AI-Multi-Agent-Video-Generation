import requests

API_KEY = "ark-7cfb3a97-7bac-406a-a775-142c1b29ea91-4f2a1"
URL = "https://ark.cn-beijing.volces.com/api/v3/chat/completions"

# 请求内容
payload = {
    "model": "ep-20260507163326-tsbjw",
    "messages": [
        {
            "role": "user",
            "content": "你好，简单介绍一下自己"
        }
    ]
}

# 请求头
headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

# 发送请求
response = requests.post(URL, json=payload, headers=headers)

# 打印结果
print("状态码:", response.status_code)
print("返回结果:", response.json())