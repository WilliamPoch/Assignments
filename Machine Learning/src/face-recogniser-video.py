import cv2
import numpy as np
from joblib import load
from sklearn.svm import SVC

HAAR_MODEL = './model-haar/haarcascade_frontalface_default.xml'
SVM_MODEL = './model-svm/gender-classify-v1.lib'

font = cv2.FONT_HERSHEY_SIMPLEX
color_William = (50,-125,125)
color_Navin = (0,255,255)
color_unknown = (200,200,200)
threshold = 0.6

detector = cv2.CascadeClassifier(HAAR_MODEL)
classifier = load(SVM_MODEL)

capture = cv2.VideoCapture(0)
capture.set(3,3000)
capture.set(4,3000)
while True:
    ret, frame = capture.read()
    image = frame.copy()
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = detector.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        testset = []
        face = gray[y:y+h, x:x+w]
        face_resized = cv2.resize(face,(256,256),interpolation=cv2.INTER_LINEAR)
        testset.append(np.ravel(face_resized))

        pred = str(classifier.predict(testset))
        prob = classifier.predict_proba(testset)
        max_prob = max(prob[0])

        if max_prob >= threshold:
            text = ''.join(pred + ' (' + '{0:.2g}'.format(max_prob * 100) + '%)')
            color = color_William
            if pred.find('Navin') != -1:
                color = color_Navin
            cv2.putText(image, text, (x,y-10), font, 0.6, color, thickness=2)
        else:
            color = color_unknown

        cv2.rectangle(image, (x,y), (x+w,y+h), color, 2)
    cv2.imshow('face classifier', image)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
capture.release()
cv2.destroyAllWindows()
