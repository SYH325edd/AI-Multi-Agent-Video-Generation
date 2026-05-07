from .base import BaseAgent

class CreativeAgent(BaseAgent):
    """创意策划Agent：接收用户原始想法，生成完整创意方案"""
    
    def run(self, user_idea: str) -> str:
        prompt = f"""
你是专业的影视创意策划师。
用户的创作想法：{user_idea}

请输出结构化的创意方案，包含以下4个部分：
1. 创意方向：一句话概括核心创意
2. 故事核心：300字以内的故事梗概
3. 风格定位：明确的视觉风格、色调、氛围描述
4. 目标时长：建议的视频时长（如30秒、1分钟、3分钟）

输出格式清晰，不要使用markdown，用数字编号分点即可。
"""
        return self.call_llm(prompt)