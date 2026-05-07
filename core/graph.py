from typing import List, Dict
from agents.base import BaseAgent
from core.state import workflow_state

class WorkflowGraph:
    """管理多Agent的串行审批式工作流"""
    def __init__(self):
        self.agents: Dict[str, BaseAgent] = {}
        # 定义流程顺序
        self.flow_order = [
            "creative", "script", "character",
            "storyboard", "unify", "film"
        ]

    def register_agent(self, name: str, agent: BaseAgent):
        self.agents[name] = agent

    def run_step(self, step: str, input_data: str) -> str:
        if step not in self.agents:
            raise ValueError(f"Agent {step} 未注册")
        
        result = self.agents[step].run(input_data)
        workflow_state.set_content(step, result)
        workflow_state.update_state(step, "done")

        # 自动解锁下一步
        current_idx = self.flow_order.index(step)
        if current_idx + 1 < len(self.flow_order):
            next_step = self.flow_order[current_idx + 1]
            workflow_state.update_state(next_step, "ready")
        
        return result

# 全局单例工作流
workflow_graph = WorkflowGraph()