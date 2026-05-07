import os
import uuid
from typing import Optional

class FileManager:
    """素材文件管理器"""
    
    def __init__(self, upload_dir: str = "data/uploads"):
        self.upload_dir = upload_dir
        os.makedirs(self.upload_dir, exist_ok=True)
    
    def save_file(self, file_content: bytes, filename: str) -> str:
        """保存上传的文件，返回文件路径"""
        # 生成唯一文件名，避免重名
        ext = os.path.splitext(filename)[1]
        unique_filename = f"{uuid.uuid4().hex}{ext}"
        file_path = os.path.join(self.upload_dir, unique_filename)
        
        with open(file_path, "wb") as f:
            f.write(file_content)
        
        return file_path
    
    def get_file(self, file_path: str) -> Optional[bytes]:
        """读取文件内容"""
        if not os.path.exists(file_path):
            return None
        with open(file_path, "rb") as f:
            return f.read()
    
    def delete_file(self, file_path: str) -> bool:
        """删除文件"""
        if os.path.exists(file_path):
            os.remove(file_path)
            return True
        return False

# 全局单例
file_manager = FileManager()