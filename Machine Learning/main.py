import cv2
#print(cv2.__version__)

faceCascade = cv2.CascadeClassifier(".\model-haar\haarscascade_frontalface_default.xml")
image = cv2.imread("i.png")

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imshow("Faces found", image)
cv2.waitKey(0)

faces = faceCascade.detectMultiScale(gray, 1.1, 5)

for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

