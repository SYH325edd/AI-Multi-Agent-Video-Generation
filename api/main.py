from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from services.workflow_service import workflow_service

app = FastAPI(title="AI多智能体视频生成系统")

# 跨域配置
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 请求模型
class UserIdeaRequest(BaseModel):
    user_idea: str

# 接口
@app.get("/api/agent/status")
def get_status():
    return workflow_service.get_status()

@app.post("/api/generate/creative")
def generate_creative(req: UserIdeaRequest):
    result = workflow_service.generate_step("creative", req.user_idea)
    return {"content": result}

@app.post("/api/confirm/creative")
def confirm_creative():
    return {"status": "ok", "state": workflow_service.confirm_step("creative")}

@app.post("/api/generate/script")
def generate_script():
    result = workflow_service.generate_step("script")
    return {"content": result}

@app.post("/api/confirm/script")
def confirm_script():
    return {"status": "ok", "state": workflow_service.confirm_step("script")}

@app.post("/api/generate/character")
def generate_character():
    result = workflow_service.generate_step("character")
    return {"content": result}

@app.post("/api/confirm/character")
def confirm_character():
    return {"status": "ok", "state": workflow_service.confirm_step("character")}

@app.post("/api/generate/storyboard")
def generate_storyboard():
    result = workflow_service.generate_step("storyboard")
    return {"content": result}

@app.post("/api/confirm/storyboard")
def confirm_storyboard():
    return {"status": "ok", "state": workflow_service.confirm_step("storyboard")}

@app.post("/api/generate/unify")
def generate_unify():
    result = workflow_service.generate_step("unify")
    return {"content": result}

@app.post("/api/confirm/unify")
def confirm_unify():
    return {"status": "ok", "state": workflow_service.confirm_step("unify")}

@app.post("/api/generate/film")
def generate_film():
    result = workflow_service.generate_step("film")
    return {"content": result}