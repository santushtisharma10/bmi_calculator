import cv2

capt = cv2.VideoCapture(0)

classifer = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

while True:

    ret, img = capt.read()

    if ret:
        faces = classifer.detectMultiScale(img)
        
        for face in faces:
            x, y, w, h = face
            img = cv2.rectangle(img, (x,y), (x+w, y+h), (255, 0, 0), 4)
        
        cv2.imshow("face detection program", img)

    key = cv2.waitKey(1)

    if key == ord("q"):
        break;

capt.release()
cv2.destroyAllWindows()