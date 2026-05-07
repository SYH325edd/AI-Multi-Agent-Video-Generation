from .base import BaseAgent

class ScriptAgent(BaseAgent):
    """剧本编撰Agent：基于创意方案生成完整分场剧本"""
    
    def run(self, creative_plan: str) -> str:
        prompt = f"""
你是专业的世界级短视频编剧。
根据以下创意方案，生成完整的分场剧本：
{creative_plan}

要求：
1. 分场编写，每场包含：场景编号、场景描述、台词、动作
2. 节奏紧凑，适合短视频观看
3. 语言口语化，符合人物身份
4. 总时长控制在创意方案建议的范围内

输出格式清晰，每场用【第X场】开头。
"""
        return self.call_llm(prompt)