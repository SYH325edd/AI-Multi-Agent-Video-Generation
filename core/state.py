from typing import Dict, Optional

class WorkflowState:
    """管理整个创作流程的状态和生成内容"""
    def __init__(self):
        # 流程状态：pending / ready / done / wait_confirm
        self.flow: Dict[str, str] = {
            "creative": "wait_confirm",
            "script": "pending",
            "character": "pending",
            "storyboard": "pending",
            "unify": "pending",
            "film": "pending"
        }
        # 存储每个环节生成的内容
        self.content: Dict[str, Optional[str]] = {
            "creative": None,
            "script": None,
            "character": None,
            "storyboard": None,
            "unify": None,
            "film": None
        }

    def update_state(self, step: str, status: str):
        self.flow[step] = status

    def set_content(self, step: str, content: str):
        self.content[step] = content

    def get_content(self, step: str) -> Optional[str]:
        return self.content.get(step)

# 全局单例状态
workflow_state = WorkflowState()