import qrcode
import os
from datetime import datetime

output_dir = "../generated_qrs"
os.makedirs(output_dir, exist_ok=True)
test_output_dir = "../../generated_qrs"

def create_qr(url : str):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"QR_{timestamp}.png"
    full_path = os.path.join(output_dir, filename)
    qr = qrcode.QRCode(version=1, box_size=10, border=4)
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(full_path)
    print(f"✅ QR-код успешно создан!")
    return os.path.abspath(full_path)


def test_create_qr(url : str):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"QR_{timestamp}.png"
    full_path = os.path.join(output_dir, filename)
    qr = qrcode.QRCode(version=1, box_size=10, border=4)
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(full_path)
    print(f"✅ QR-код успешно создан!")
    return os.path.abspath(full_path)