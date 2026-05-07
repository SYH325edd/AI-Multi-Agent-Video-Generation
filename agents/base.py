from core.llm import llm_client

class BaseAgent:
    """所有Agent的基类，统一使用core/llm.py里的大模型客户端"""
    
    def call_llm(self, prompt: str) -> str:
        """调用大模型，返回生成结果"""
        return llm_client.generate(prompt)
    
    def run(self, input_data: str) -> str:
        """每个Agent必须实现的核心方法"""
        raise NotImplementedError("子类必须实现run方法")