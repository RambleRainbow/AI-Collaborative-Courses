import json
import os
from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel

app = FastAPI()

# 1. 静态文件服务
# Mount media directory for videos
app.mount("/media", StaticFiles(directory="media"), name="media")
# Mount src directory for raw code reading (optional, mostly handled by API)
# app.mount("/src", StaticFiles(directory="src"), name="src")

@app.get("/")
async def read_index():
    return FileResponse('index.html')

# 2. API: 获取分镜列表
@app.get("/api/scenes")
async def get_scenes():
    try:
        with open("scripts.json", "r", encoding="utf-8") as f:
            data = json.load(f)
        return data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# 3. API: 获取代码内容
@app.get("/api/code")
async def get_code(path: str):
    # 安全检查: 简单防止路径遍历 (只允许当前目录下的src)
    clean_path = os.path.normpath(path)
    if not clean_path.startswith("src/"):
        raise HTTPException(status_code=403, detail="Access denied")
    
    if not os.path.exists(clean_path):
        raise HTTPException(status_code=404, detail="File not found")
        
    try:
        with open(clean_path, "r", encoding="utf-8") as f:
            content = f.read()
        return {"content": content}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    print("启动服务器: http://127.0.0.1:8000")
    uvicorn.run(app, host="127.0.0.1", port=8000)
