from .base import BaseAgent

class QAAgent(BaseAgent):
    """质检Agent：检查生成内容的质量、逻辑、一致性"""
    
    def run(self, content: str, content_type: str) -> str:
        prompt = f"""
你是专业的内容质检员。
检查以下{content_type}的质量：
{content}

检查要点：
1. 逻辑是否通顺
2. 是否有前后矛盾的地方
3. 是否符合要求的格式
4. 是否有明显的错误

输出检查结果和修改建议。
"""
        return self.call_llm(prompt)