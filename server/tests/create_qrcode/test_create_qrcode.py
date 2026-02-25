from server.src.create_qrcode import create_qr
import os


def test_create_qr():
    res = create_qr("test")
    file_name = os.path.basename(res)
    assert res.endswith(".png")
    assert file_name.startswith("QR")
    os.system("rm -rf ../generated_qrs")
