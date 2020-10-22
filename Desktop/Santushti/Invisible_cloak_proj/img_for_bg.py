import cv2

bg = cv2.VideoCapture(0)
bg.set(3, 1200)
bg.set(4, 1000)

while True:

    ret, img = bg.read()
    
    if ret:
        cv2.imshow("sample", img)
        
    if cv2.waitKey(1) == ord("q"):
        cv2.imwrite("bg_image.jpg", img)
        break;

bg.release()
cv2.destroyAllWindows()
