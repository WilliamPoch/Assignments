import cv2
from pathlib import Path

detector = cv2.CascadeClassifier('./model-haar/cascade.xml')

font = cv2.FONT_HERSHEY_SIMPLEX
color = (0,0,255)

image = cv2.imread('./samples/sample0')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
faces = detector.detectMultiScale(gray, 1.3, 5)

for (x, y, w, h) in faces:
    face = image[y:y+h, x:x+w]
    cv2.rectangle(image, (x,y), (x+w,y+h), color, 2)

cv2.imshow('My Face Detector', image)
cv2.imwrite('./samples/output.jpg', image)
cv2.waitKey(0)
cv2.destroyAllWindows()