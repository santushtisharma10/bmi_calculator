import pytesseract
import cv2

img = cv2.imread("WhatsApp Image 2020-09-07 at 14.19.53.jpeg")


#img = cv2.resize(img, (1180, 780))

cv2.waitKey(0)
img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
str1 = [pytesseract.image_to_string(img)]

print(str1)


cv2.imshow("img", img)
cv2.waitKey(0)

print("Success")
