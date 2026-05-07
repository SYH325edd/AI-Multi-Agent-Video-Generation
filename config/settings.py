from pydantic_settings import BaseSettings
from dotenv import load_dotenv
import os

# 加载.env文件
load_dotenv()

class Settings(BaseSettings):
    # 大模型配置
    ARK_API_KEY: str = os.getenv("ARK_API_KEY", "")
    ARK_URL: str = "https://ark.cn-beijing.volces.com/api/v3/chat/completions"
    MODEL_ID: str = "ep-20260507163326-tsbjw"
    MAX_TOKENS: int = 2048
    TEMPERATURE: float = 0.7

    # 服务配置
    HOST: str = "127.0.0.1"
    PORT: int = 8001
    DEBUG: bool = True

    # Agent开关配置
    ENABLE_CREATIVE_AGENT: bool = True
    ENABLE_SCRIPT_AGENT: bool = True
    ENABLE_CHARACTER_AGENT: bool = True
    ENABLE_STORYBOARD_AGENT: bool = True
    ENABLE_UNIFY_AGENT: bool = True
    ENABLE_FILM_AGENT: bool = True
    ENABLE_QA_AGENT: bool = True

    class Config:
        env_file = ".env"
        case_sensitive = True

# 全局配置实例
settings = Settings()