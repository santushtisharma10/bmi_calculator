import cv2
import numpy as np

cap = cv2.VideoCapture(0)
cap.set(3, 1200)
cap.set(4, 1000)

bg_img = cv2.imread("bg_image.jpg")

blue = np.uint8([[[255, 0, 0]]])
hsv_blue = cv2.cvtColor(blue, cv2.COLOR_BGR2HSV)
lower = np.array([110, 100, 100])
upper = np.array([130, 255, 255])
while True:

    ret, img = cap.read()
    
    if ret:
        
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv, lower, upper)
        #cv2.imshow("hsv", mask)hs
        
        part1 = cv2.bitwise_and(bg_img, bg_img, mask=mask)
        mask = cv2.bitwise_not(mask)
        part2 = cv2.bitwise_and(img, img, mask=mask)
        cv2.imshow("proj", part1+part2)

    if cv2.waitKey(1) == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
