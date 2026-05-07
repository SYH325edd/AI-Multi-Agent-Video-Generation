from .base import BaseAgent

class FilmAgent(BaseAgent):
    """成片生成Agent：将校准后的分镜转化为视频生成提示词"""
    
    def run(self, unified_storyboard: str) -> str:
        prompt = f"""
你是专业的视频生成提示词工程师。
根据以下校准后的分镜脚本，生成适合AI视频生成工具的提示词：
{unified_storyboard}

要求：
1. 每个镜头生成独立的视频提示词
2. 包含镜头运动、转场效果、背景音乐建议
3. 保持所有镜头的风格一致性
4. 提示词简洁准确，符合主流视频生成工具的规范

输出格式清晰，每个镜头用【镜头X提示词】开头。
"""
        return self.call_llm(prompt)