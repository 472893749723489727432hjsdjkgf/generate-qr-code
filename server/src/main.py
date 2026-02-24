from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse,Response
from pydantic import BaseModel
from db import init_tables,sendData
from create_qrcode import create_qr
from pathlib import Path
from contextlib import asynccontextmanager
import uvicorn
import os


CLIENT_DIR = Path("../../client").resolve()


class QrSchema(BaseModel):
    url : str

@asynccontextmanager
async def lifespan(app : FastAPI):
    await init_tables()
    print("таблицы созданы")
    os.system("rm -rf ../generated_qrs* && mkdir ../generated_qrs ")
    print("Папка с qr кодом очищена!")
    yield

app = FastAPI(lifespan=lifespan)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return FileResponse(path=CLIENT_DIR/"index.html")




@app.get("/api/get_img")
async def sendImgOnFront(file_path: str):
    abs_path = os.path.abspath(file_path)
    if os.path.exists(abs_path):
        return FileResponse(abs_path)
    return Response(status_code=404, content="File not found")



@app.post("/api/send_url")
async def generate_qr(data: QrSchema):
    try:
        file_path = create_qr(data.url)
        await sendData(file_path, data.url)


        return {"file_path": file_path}

    except Exception as e:
        print(f"Error: {e}")
        raise HTTPException(status_code=500, detail=str(e))



if __name__ == "__main__":
    uvicorn.run("main:app",reload=True,port=8080)