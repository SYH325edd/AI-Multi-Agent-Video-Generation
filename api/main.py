from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import os
import time
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(title="AI影视创作系统")

# 跨域（必须加，否则前端永远连不上）
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 全局流程状态
flow_state = {
    "creative": "wait_confirm",
    "script": "pending",
    "character": "pending",
    "storyboard": "pending",
    "unify": "pending",
    "film": "pending"
}

# ------------------------------
# 前端必用的接口
# ------------------------------
@app.get("/api/agent/status")
def get_status():
    return flow_state

@app.post("/api/confirm/creative")
def confirm_creative():
    flow_state["creative"] = "done"
    flow_state["script"] = "ready"
    return {"status": "ok", "state": flow_state}

@app.post("/api/confirm/script")
def confirm_script():
    flow_state["script"] = "done"
    flow_state["character"] = "ready"
    return {"status": "ok", "state": flow_state}

@app.post("/api/confirm/character")
def confirm_character():
    flow_state["character"] = "done"
    flow_state["storyboard"] = "ready"
    return {"status": "ok", "state": flow_state}

@app.post("/api/confirm/storyboard")
def confirm_storyboard():
    flow_state["storyboard"] = "done"
    flow_state["unify"] = "ready"
    return {"status": "ok", "state": flow_state}

@app.post("/api/confirm/unify")
def confirm_unify():
    flow_state["unify"] = "done"
    flow_state["film"] = "ready"
    return {"status": "ok", "state": flow_state}

# 模拟生成内容
@app.post("/api/generate/creative")
def generate_creative():
    time.sleep(1)
    return {"content": "已生成创意方案：科幻短片，未来宇宙探索故事"}

@app.post("/api/generate/script")
def generate_script():
    time.sleep(1)
    return {"content": "已生成完整剧本：共5场戏，主角驾驶飞船发现神秘星球"}

@app.post("/api/generate/character")
def generate_character():
    time.sleep(1)
    return {"content": "已生成角色：宇航员、AI助手、外星生命"}

@app.post("/api/generate/storyboard")
def generate_storyboard():
    time.sleep(1)
    return {"content": "已生成分镜：共12个镜头，飞船起飞、降落、探索"}

@app.post("/api/generate/unify")
def generate_unify():
    time.sleep(1)
    return {"content": "已完成视觉校准：人物统一、色调统一、风格统一"}

@app.post("/api/generate/film")
def generate_film():
    time.sleep(1)
    return {"content": "已生成最终成片：4K科幻短片"}