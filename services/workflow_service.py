from data.project_manager import project_manager
from core.graph import workflow_graph
from core.state import workflow_state
from typing import Optional

class WorkflowService:
    """工作流业务服务，封装所有创作流程逻辑"""
    
    def __init__(self):
        # 默认使用一个全局项目ID，后续可以扩展多项目
        self.default_project_id = "default_project"
        # 初始化默认项目
        if not project_manager.load_project(self.default_project_id):
            project_manager.create_project(self.default_project_id, "默认影视项目")
        # 同步本地数据到全局状态
        self._sync_state_from_db()
    
    def _sync_state_from_db(self):
        """从数据库同步状态到全局内存"""
        project = project_manager.load_project(self.default_project_id)
        if project:
            workflow_state.flow = project["flow_state"]
            workflow_state.content = project["content"]
    
    def _sync_state_to_db(self):
        """把全局内存状态同步到数据库"""
        project = project_manager.load_project(self.default_project_id)
        if project:
            project["flow_state"] = workflow_state.flow
            project["content"] = workflow_state.content
            project_manager.save_project(self.default_project_id, project)
    
    def get_status(self):
        """获取当前流程状态"""
        self._sync_state_from_db()
        return workflow_state.flow
    
    def generate_step(self, step: str, input_data: Optional[str] = None) -> str:
        """生成某个步骤的内容"""
        if input_data:
            result = workflow_graph.run_step(step, input_data)
        else:
            # 如果没有输入数据，就用前一步的输出
            prev_step = self._get_prev_step(step)
            prev_content = workflow_state.get_content(prev_step)
            result = workflow_graph.run_step(step, prev_content)
        
        # 保存到数据库
        project_manager.update_content(self.default_project_id, step, result)
        self._sync_state_to_db()
        return result
    
    def confirm_step(self, step: str):
        """确认某个步骤，解锁下一步"""
        workflow_state.update_state(step, "done")
        next_step = self._get_next_step(step)
        if next_step:
            workflow_state.update_state(next_step, "ready")
        
        # 保存到数据库
        project_manager.update_flow_state(self.default_project_id, step, "done")
        if next_step:
            project_manager.update_flow_state(self.default_project_id, next_step, "ready")
        
        return workflow_state.flow
    
    def _get_prev_step(self, step: str) -> Optional[str]:
        """获取上一个步骤"""
        flow_order = ["creative", "script", "character", "storyboard", "unify", "film"]
        idx = flow_order.index(step)
        return flow_order[idx-1] if idx > 0 else None
    
    def _get_next_step(self, step: str) -> Optional[str]:
        """获取下一个步骤"""
        flow_order = ["creative", "script", "character", "storyboard", "unify", "film"]
        idx = flow_order.index(step)
        return flow_order[idx+1] if idx < len(flow_order)-1 else None

# 全局单例
workflow_service = WorkflowService()