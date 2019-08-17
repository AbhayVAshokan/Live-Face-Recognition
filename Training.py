import cv2
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Convolution2D, MaxPooling2D, Flatten, Reshape
from sklearn.model_selection import train_test_split
from tensorflow.keras.preprocessing.image import ImageDataGenerator

def train(X, y):
    N = np.unique(y).size

    model = Sequential()
    model.add(Reshape((64, 64, 1)))
    model.add(Convolution2D(32, (3, 3), input_shape = (64, 64), activation = 'relu'))
    model.add(MaxPooling2D(pool_size = (2, 2)))
    model.add(Convolution2D(16, (3, 3),  activation = 'relu'))
    model.add(MaxPooling2D(pool_size = (2, 2)))
    model.add(Flatten())
    model.add(Dense(units = 128, activation = 'relu'))
    model.add(Dense(units = 128, activation = 'relu'))
    model.add(Dense(units = N, activation = 'softmax'))

    model.compile(optimizer = 'adam', metrics = ['accuracy'], loss = 'sparse_categorical_crossentropy')

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.1)

    number_of_training_samples = len(list(X_train))
    number_of_testing_samples = len(list(X_test))
    X_train = X_train.reshape((number_of_training_samples, 64, 64, 1))
    X_test = X_test.reshape((number_of_testing_samples, 64, 64, 1))

    datagen = ImageDataGenerator(width_shift_range=0.1,
                                height_shift_range=0.1,
                                zoom_range=0.2,
                                shear_range=0.1,
                                rotation_range=10.)

    datagen.fit(X_train)
    batches = datagen.flow(X_train, y_train, batch_size = 15)
    X_batch, y_batch = next(batches)

    model.fit_generator(datagen.flow(X_train, y_train, batch_size = 50),
                            steps_per_epoch = 2 * number_of_training_samples,
                            epochs=1, validation_data = (X_test, y_test))

    return model
