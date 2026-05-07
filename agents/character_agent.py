from .base import BaseAgent

class CharacterAgent(BaseAgent):
    """角色设计Agent：根据剧本生成所有角色的详细设定"""
    
    def run(self, script: str) -> str:
        prompt = f"""
你是专业的影视角色设计师。
根据以下剧本，设计所有出现的角色：
{script}

每个角色需要包含：
1. 姓名
2. 年龄、性别
3. 外貌特征（发型、服装、体型）
4. 性格特点
5. 视觉风格参考（适合AI绘画的描述）

输出格式清晰，每个角色用【角色X：姓名】开头。
"""
        return self.call_llm(prompt)