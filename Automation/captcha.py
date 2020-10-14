import pytesseract
from PIL import Image
from cv2 import cv2


class img_txt:
    def __init__(self, image):
        self.image = image

    def txt(self):
        img = cv2.imread(self.image, 0)
        # img = cv2.medianBlur(img, 5)

        #  Otsu's thresholding after Gaussian filtering
        blur = cv2.GaussianBlur(img, (5, 5), 0)
        ret, th3 = cv2.threshold(
            blur, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
        pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
        cv2.imwrite('captcha_text.png', th3)
        txt = pytesseract.image_to_string(
            Image.open('captcha_text.png'), lang="eng").strip()
        print(txt)
        return txt
