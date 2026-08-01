import qrcode
import os

from datetime import datetime

#output_dir = "../generated_qrs"




class CreateQrCode:
    def __init__(self,url : str,output_dir : str):
        self.url = url
        self.output_dir = output_dir
        os.makedirs(output_dir, exist_ok=True)

    def create_qr_code(self) -> str:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"QR_{timestamp}.png"
        full_path = os.path.join(self.output_dir,filename)
        qr = qrcode.QRCode(version=1,box_size=10,border=4)
        qr.add_data(self.url)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black",back_color="white")
        img.save(full_path)
        print(f"✅ QR-код успешно создан!")
        return os.path.abspath(full_path)






