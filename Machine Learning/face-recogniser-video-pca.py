import cv2
import numpy as np
from joblib import load

from sklearn.decomposition import PCA
from sklearn.svm import SVC

HAAR_MODEL = './model-haar/haarcascade_frontalface_default.xml'
SVM_MODEL = './model-svm/gender-classify-v1.lib'

font = cv2.FONT_HERSHEY_SIMPLEX
color_male = (255,0,0)
color_female = (100,100,255)
color_unknown = (200,200,200)
labels = ['2','1']

detector = cv2.CascadeClassifier(HAAR_MODEL)
classifier = load(SVM_MODEL)

capture = cv2.VideoCapture('rtsp://admin:islabac123@192.168.1.201')
while True:
    ret, frame = capture.read()
    image = frame.copy()
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = detector.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        testset = []
        face = gray[y:y+h, x:x+w]
        face_resized = cv2.resize(face,(256,256), interpolation=cv2.INTER_LINEAR)
        testset.append(np.ravel(face_resized))

        pca = load('./model-svm/pca.lib')
        features = pca.transform(testset)

        pred = int(classifier.predict(features))
        max_prob = 10
        threshold = 0

        text = ''.join(labels[pred])
        color = color_male
        if (pred == 0):
            color = color_female
        cv2.putText(image, text, (x,y-10), font, 0.6, color, thickness=2)

        cv2.rectangle(image, (x,y), (x+w,y+h), color, 2)
    cv2.imshow('face classifier', image)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
capture.release()
cv2.destroyAllWindows()
