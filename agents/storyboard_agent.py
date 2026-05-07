from .base import BaseAgent

class StoryboardAgent(BaseAgent):
    """分镜设计Agent：根据剧本和角色生成逐镜头分镜脚本"""
    
    def run(self, character_and_script: str) -> str:
        prompt = f"""
你是专业的分镜师。
根据以下剧本和角色设定，生成逐镜头分镜脚本：
{character_and_script}

每个镜头需要包含：
1. 镜头编号
2. 镜头类型（全景/中景/近景/特写）
3. 画面描述（详细到可以直接用于AI绘画）
4. 时长（秒）
5. 台词/旁白

输出格式清晰，每个镜头用【镜头X】开头。
"""
        return self.call_llm(prompt)