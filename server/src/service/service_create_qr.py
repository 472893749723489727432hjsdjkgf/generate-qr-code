from qr_gen.create_qr_code import CreateQrCode


async def qr_gen(url : str) -> str:
    create_qr = CreateQrCode(url,"../generated_qrs")
    path = create_qr.create_qr_code()
    return path


