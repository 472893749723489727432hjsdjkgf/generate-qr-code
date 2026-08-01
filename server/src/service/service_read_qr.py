from qr_gen.read_qr_code import ReadQrCode


async def read_qr(img_path : str) -> str:
    qr_reader = ReadQrCode(img_path)
    data = qr_reader.read_qr()
    return data

