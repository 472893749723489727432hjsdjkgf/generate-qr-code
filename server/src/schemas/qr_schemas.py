from pydantic import BaseModel

class QrCreateSchema(BaseModel):
    url : str

class QrReadSchema(BaseModel):
    img_path : str
