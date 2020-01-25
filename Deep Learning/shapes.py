import os
import numpy as np
import cv2

images = []
labels = []
img_size = 28

label = ['circle', 'square', 'star', 'triangle']
for folder in label:
    for path in os.listdir(os.getcwd()+'\\'+folder): #os.getcwd() to get current directory
        img = cv2.imread(folder + '\\' + path, 0) #Read image and convert to greyscale using cv2
        images.append(cv2.resize(img, (img_size, img_size))) #Resize to 28x28
        labels.append(label.index(folder)) #Appends either 0, 1, 2, or 3 depending on the folder


#Convert to numpy arrays
images = np.array(images)
labels = np.array(labels)
#print(images.shape)
#Reshape images to fit the format of (samples, height, width, channels)
images = images.reshape(len(images), img_size, img_size, 1)
#print(images.shape)


#Split into test and training sets
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(images, labels, test_size=0.3,
                                                    random_state=42)


#Convert labels to categorical using one_hot
import keras
from keras.utils import np_utils
y_train = keras.utils.to_categorical(y_train, len(np.unique(labels)))
y_test = keras.utils.to_categorical(y_test, len(np.unique(labels)))

#Create the model
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout
from keras.layers import Flatten
from keras import optimizers

model = Sequential()
model.add(Flatten(input_shape=(28, 28, 1)))
model.add(Dense(128, activation='tanh'))
model.add(Dropout(0.3))
model.add(Dense(128, activation='relu'))
model.add(Dense(4, activation='softmax'))
sgd = optimizers.SGD(lr=0.01, nesterov=True)
model.compile(optimizer=sgd, loss='categorical_crossentropy', metrics=['accuracy'])


from keras.preprocessing.image import ImageDataGenerator
#Perform image preprocessing on train set
train_datagen = ImageDataGenerator(rescale=1. / 255, shear_range=0.5, zoom_range=0.2,
                                   horizontal_flip=True,
                                   width_shift_range=2,
                                   height_shift_range=2,
                                   vertical_flip=True)
test_datagen = ImageDataGenerator(rescale=1. / 255)


train_datagen = train_datagen.flow(X_train, y_train, batch_size=32)
test_datagen = test_datagen.flow(X_test, y_test, batch_size=32)



model.fit_generator(train_datagen,
                    steps_per_epoch=len(X_train)/32,
                    epochs=30,
                    validation_data=test_datagen,
                    validation_steps=len(X_test)/32)

model.summary()
#Save whole model or just weights
#model.save('shape.h5')
#model.save_weights('shape_weights.h5')

#Evaluate on test set
eval = model.evaluate_generator(test_datagen, len(X_test))
print('Loss and Accuracy score on test set: ', eval)


