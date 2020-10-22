import cv2
import numpy as np

img = cv2.imread("Hp\Desktop\Santushti\Open_Source\cards.jpg")
act = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


#width = 250
#height = 350

#pt1 = np.float32([[86, 36], [192, 21], [109, 202], [217, 188]])
#pt2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])

#Mat = cv2.getPerspectiveTransform(pt1, pt2)

#warpimg = cv2.warpPerspective(img, Mat, (width, height))
hor = np.hstack([img, act, img, act])

cv2.imshow("horizontal image", hor)

#cv2.imshow("output", warpimg)
cv2.waitKey(0)