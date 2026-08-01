import cv2
import os

class ReadQrCode:
    def __init__(self,img_path : str):
        self.img = cv2.imread(img_path)
        self.img_path = img_path
    def read_qr(self) -> str:
        detector = cv2.QRCodeDetector()
        data, _, _ = detector.detectAndDecode(self.img)
        if data:
            os.remove(self.img_path)
            return data
        return "Qr не распознан"




