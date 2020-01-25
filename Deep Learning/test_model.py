import cv2, numpy as np
from keras.models import load_model
#from PIL import Image
#import matplotlib as plt
model = load_model('shape.h5')


def get_label(num):
    if (num == 0):
        return 'circle'
    elif (num == 1):
        return 'square'
    elif (num == 2):
        return 'star'
    else:
        return 'triangle'

path = 'test/test8.png'
path = cv2.imread(path, 0)
img = (cv2.resize(path, (28, 28)))
img = img.reshape(1, 28, 28, 1)
pred = model.predict(img)
pred = np.argmax(pred, axis=1)
cv2.namedWindow(get_label(pred), cv2.WINDOW_NORMAL)
cv2.resizeWindow(get_label(pred), 300, 300)
cv2.imshow(get_label(pred), path)
cv2.waitKey(0)
cv2.destroyAllWindows()

