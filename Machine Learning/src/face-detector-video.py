import cv2
import numpy as np
from pathlib import Path

detector = cv2.CascadeClassifier('./model-haar/fb_cascade.xml')
font = cv2.FONT_HERSHEY_SIMPLEX
color = (0,255,0)

capture = cv2.VideoCapture(0)
while True:
    ret, frame = capture.read()
    image = frame.copy()
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = detector.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        face = image[y:y+h, x:x+w]
        cv2.rectangle(image, (x,y), (x+w,y+h), color, 2)

    cv2.imshow('My Face Detector', image)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
capture.release()
cv2.destroyAllWindows()
