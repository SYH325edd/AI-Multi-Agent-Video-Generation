from .base import BaseAgent

class UnifyAgent(BaseAgent):
    """视觉风格校准Agent：统一所有分镜的色调、人物、风格、提示词规范"""
    
    def run(self, storyboard: str) -> str:
        prompt = f"""
你是专业的视觉校准师，负责统一所有AI生成内容的风格。
根据以下分镜脚本，完成以下4项校准工作：
{storyboard}

1. 人物形象统一：所有镜头中的同一个人物，外貌、服装、发型必须完全一致
2. 色调风格统一：所有镜头使用相同的色调、光影、氛围
3. 提示词规范统一：将每个镜头的画面描述转化为标准化的AI绘画提示词
4. 画面质感统一：所有镜头使用相同的画质、分辨率、艺术风格

输出格式：每个镜头保留原编号，后面跟上校准后的标准化提示词。
"""
        return self.call_llm(prompt)