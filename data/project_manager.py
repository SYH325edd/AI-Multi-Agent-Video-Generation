import json
import os
from typing import Dict, Optional

class ProjectManager:
    """项目数据管理器，负责持久化存储所有项目数据"""
    
    def __init__(self, data_dir: str = "data/projects"):
        self.data_dir = data_dir
        os.makedirs(self.data_dir, exist_ok=True)
    
    def create_project(self, project_id: str, project_name: str) -> Dict:
        """创建一个新项目"""
        project_data = {
            "project_id": project_id,
            "project_name": project_name,
            "created_at": os.times()[0],
            "updated_at": os.times()[0],
            "flow_state": {
                "creative": "wait_confirm",
                "script": "pending",
                "character": "pending",
                "storyboard": "pending",
                "unify": "pending",
                "film": "pending"
            },
            "content": {
                "creative": None,
                "script": None,
                "character": None,
                "storyboard": None,
                "unify": None,
                "film": None
            }
        }
        self.save_project(project_id, project_data)
        return project_data
    
    def save_project(self, project_id: str, project_data: Dict):
        """保存项目数据到本地文件"""
        file_path = os.path.join(self.data_dir, f"{project_id}.json")
        project_data["updated_at"] = os.times()[0]
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(project_data, f, ensure_ascii=False, indent=2)
    
    def load_project(self, project_id: str) -> Optional[Dict]:
        """从本地文件加载项目数据"""
        file_path = os.path.join(self.data_dir, f"{project_id}.json")
        if not os.path.exists(file_path):
            return None
        with open(file_path, "r", encoding="utf-8") as f:
            return json.load(f)
    
    def update_content(self, project_id: str, step: str, content: str):
        """更新某个步骤的生成内容"""
        project = self.load_project(project_id)
        if project:
            project["content"][step] = content
            self.save_project(project_id, project)
    
    def update_flow_state(self, project_id: str, step: str, status: str):
        """更新某个步骤的流程状态"""
        project = self.load_project(project_id)
        if project:
            project["flow_state"][step] = status
            self.save_project(project_id, project)

# 全局单例
project_manager = ProjectManager()