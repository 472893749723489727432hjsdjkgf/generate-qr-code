from fastapi import APIRouter
from fastapi.responses import FileResponse
from service.service_read_qr import read_qr
from service.service_create_qr import qr_gen
from schemas.qr_schemas import QrCreateSchema,QrReadSchema

qr_router = APIRouter(prefix="/api/qr")

@qr_router.post("/generate_qrcode")
async def create_qr_code_router(data : QrCreateSchema) ->  FileResponse:
    img_path = await qr_gen(data.url)
    return FileResponse(img_path,media_type="image/png")

@qr_router.post("/read_qrcode")
async def read_qr_code_router(data : QrReadSchema) -> dict[str,str]:
    data = await read_qr(data.img_path)
    return {
        "data" : data
    }

    