from core.llm import call_llm
from config.settings import SCRIPT_MODEL


def script_agent(state):

    prompt = """
你是影视剧本分析AI、世界顶级导演、摄影师。
输出必须是JSON结构：
{
  "theme": "",
  "characters": [],
  "scenes": []
}
"""

    result = call_llm(prompt, state.input_text, SCRIPT_MODEL)

    # 写入全局状态
    state.script_result = result
    state.logs.append("script_agent完成")

    return state