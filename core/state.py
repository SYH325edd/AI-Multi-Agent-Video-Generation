from typing import Dict, Any, List


class GlobalState:
    """
    多Agent共享数据中心
    所有AI的输出都写进这里
    """

    def __init__(self):

        # 用户输入
        self.input_text: str = ""

        # 剧本分析结果
        self.script_result: Dict[str, Any] = {}

        # 分镜结果
        self.storyboard: List[Dict[str, Any]] = []

        # prompt结果
        self.prompts: List[str] = []

        # 视觉结果
        self.images: List[str] = []

        # 日志（非常重要）
        self.logs: List[str] = []

        # 当前状态
        self.status: str = "idle"