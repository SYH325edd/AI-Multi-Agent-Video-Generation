from config.settings import settings
import requests
from typing import Optional

class LLMClient:
    """统一的大模型调用客户端，所有Agent都通过它来调用模型"""
    def __init__(self):
        self.api_key = settings.ARK_API_KEY
        self.url = settings.ARK_URL
        self.model = settings.MODEL_ID
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

    def generate(self, prompt: str, temperature: Optional[float] = None) -> str:
        payload = {
            "model": self.model,
            "messages": [{"role": "user", "content": prompt}],
            "temperature": temperature or settings.TEMPERATURE,
            "max_tokens": settings.MAX_TOKENS
        }
        try:
            resp = requests.post(self.url, json=payload, headers=self.headers, timeout=30)
            resp.raise_for_status()
            return resp.json()["choices"][0]["message"]["content"].strip()
        except Exception as e:
            return f"LLM调用失败：{str(e)}"

# 全局单例，所有模块共享同一个客户端
llm_client = LLMClient()