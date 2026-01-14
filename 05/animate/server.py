import json
import os
from fastapi import FastAPI, HTTPException, WebSocket
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import asyncio
import subprocess

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False, # Changed to False to avoid 403 with wildcard origin
    allow_methods=["*"],
    allow_headers=["*"],
)

# 1. 静态文件服务
# Mount media directory for videos
os.makedirs("media", exist_ok=True) # Ensure directory exists
app.mount("/media", StaticFiles(directory="media"), name="media")
# Mount src directory for raw code reading (optional, mostly handled by API)
# app.mount("/src", StaticFiles(directory="src"), name="src")

class SceneData(BaseModel):
    id: str
    desc: str
    code_content: str  # New field for saving code

@app.get("/", response_class=HTMLResponse)
async def read_root():
    with open("index.html", "r", encoding="utf-8") as f:
        return HTMLResponse(content=f.read())

# 2. API: 获取分镜列表
@app.get("/api/scenes")
async def get_scenes():
    try:
        with open("scripts.json", "r", encoding="utf-8") as f:
            data = json.load(f)
        
        # Dynamic path resolution
        # Search priorities
        qualities = ["1080p60", "720p60", "480p15"] 
        
        for item in data:
            # Check configured path first
            if os.path.exists(item.get("video_path", "")): continue
                
            # Try to resolve based on code_path and scene_class
            # code_path: src/act1/scene1.py -> module_name: scene1
            # structure: media/videos/{module_name}/{quality}/{SceneClass}.mp4
            
            try:
                code_path = item.get("code_path", "")
                scene_class = item.get("scene_class", "")
                if code_path and scene_class:
                    module_name = os.path.splitext(os.path.basename(code_path))[0]
                    
                    found = False
                    for q in qualities:
                        # Construct potential path
                        # Note: relative to project root
                        candidate = f"media/videos/{module_name}/{q}/{scene_class}.mp4"
                        if os.path.exists(candidate):
                            item["video_path"] = candidate
                            found = True
                            break
                    
                    if not found and not item.get("video_path"):
                        # Keep default but maybe empty? or keep 1080p60 as target
                        pass
            except Exception as e:
                print(f"Error resolving path for {item.get('id')}: {e}")

        return data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# 3. API: 获取代码内容
@app.get("/api/code")
async def get_code(path: str):
    # 安全检查: 简单防止路径遍历 (只允许当前目录下的src)
    # clean_path = os.path.normpath(path)
    # if not clean_path.startswith("src/"):
    #     raise HTTPException(status_code=403, detail="Access denied")
    
    if not os.path.exists(path):
        raise HTTPException(status_code=404, detail="File not found")
        
    try:
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
        return {"content": content}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.websocket("/ws/render")
async def websocket_render(websocket: WebSocket, id: str):
    print(f"WS Connection Request: {id}") # Debug log
    await websocket.accept()
    print("WS Connected")
    try:
        # Find scene info
        with open("scripts.json", "r", encoding="utf-8") as f:
            scenes = json.load(f)
        scene = next((s for s in scenes if s["id"] == id), None)
        
        if not scene:
            await websocket.send_text("Error: Scene ID not found.\n")
            await websocket.close()
            return

        cmd = ["uv", "run", "manim", "-pql", scene["code_path"], scene["scene_class"]]
        # Force flush to ensure real-time output
        
        await websocket.send_text(f"Executing: {' '.join(cmd)}\n\n")
        
        # Add PYTHONPATH to include project root so 'from src.utils import *' works
        env = os.environ.copy()
        env["PYTHONPATH"] = os.getcwd() + os.pathsep + env.get("PYTHONPATH", "")

        process = await asyncio.create_subprocess_exec(
            *cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            env=env
        )

        async def read_stream(stream, label):
            while True:
                line = await stream.readline()
                if not line: break
                text = line.decode('utf-8', errors='replace')
                await websocket.send_text(text)

        await asyncio.gather(
            read_stream(process.stdout, "stdout"),
            read_stream(process.stderr, "stderr")
        )

        exit_code = await process.wait()
        await websocket.send_text(f"\nProcess finished with exit code {exit_code}")
        
        # Signal completion to frontend
        if exit_code == 0:
            await websocket.send_text("###DONE###")
        
    except Exception as e:
        print(f"WS Error: {e}")
        try:
            await websocket.send_text(f"Server Error: {str(e)}")
        except: pass
    finally:
        try:
            await websocket.close()
        except: pass

if __name__ == "__main__":
    import uvicorn
    print("启动服务器: http://127.0.0.1:8000")
    uvicorn.run(app, host="127.0.0.1", port=8000)
