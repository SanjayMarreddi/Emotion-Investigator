# First let us Import Libraries

import utils
import os
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

get_ipython().run_line_magic('matplotlib', 'inline')

from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.layers import Dense, Input, Dropout,Flatten, Conv2D
from tensorflow.keras.layers import BatchNormalization, Activation, MaxPooling2D
from tensorflow.keras.models import Model, Sequential
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.callbacks import ModelCheckpoint, ReduceLROnPlateau
from tensorflow.keras.utils import plot_model
from IPython.display import SVG, Image
from livelossplot import PlotLossesKerasTF
import tensorflow as tf

print("Tensorflow version:", tf.__version__)




# Now let us Generate Training and Validation Batches

batch_size = 128
img_size = 48

datagen_train = ImageDataGenerator(horizontal_flip=True)

train_generator = datagen_train.flow_from_directory("train/",
                                                    target_size=(img_size,img_size),
                                                    color_mode="grayscale",
                                                    batch_size=batch_size,
                                                    class_mode='categorical',
                                                    shuffle=True)

datagen_validation = ImageDataGenerator(horizontal_flip=True)
validation_generator = datagen_validation.flow_from_directory("test/",
                                                    target_size=(img_size,img_size),
                                                    color_mode="grayscale",
                                                    batch_size=batch_size,
                                                    class_mode='categorical',
                                                    shuffle=False)


#  Create CNN Model


# Initialising the CNN
model = Sequential()

# 1 - Convolution
model.add(Conv2D(64,(3,3), padding='same', input_shape=(48, 48,1)))
model.add(BatchNormalization())
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.5))

# 2nd Convolution layer
model.add(Conv2D(128,(5,5), padding='same'))
model.add(BatchNormalization())
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.6))

# 3rd Convolution layer
model.add(Conv2D(128,(5,5), padding='same'))
model.add(BatchNormalization())
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.7))

# 4th Convolution layer
model.add(Conv2D(512,(3,3), padding='same'))
model.add(BatchNormalization())
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.8))


# 5th Convolution layer
model.add(Conv2D(512,(3,3), padding='same'))
model.add(BatchNormalization())
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.8))


# Flattening
model.add(Flatten())

# Fully connected layer 1st layer
model.add(Dense(256))
model.add(BatchNormalization())
model.add(Activation('relu'))
model.add(Dropout(0.6))

# Fully connected layer 2nd layer
model.add(Dense(512))
model.add(BatchNormalization())
model.add(Activation('relu'))
model.add(Dropout(0.6))

model.add(Dense(7, activation='softmax'))

opt = Adam(lr=0.01)
model.compile(optimizer=opt, loss='categorical_crossentropy', metrics=['accuracy'])
model.summary()


# Train and Evaluate Model


get_ipython().run_cell_magic('time', '', '\nepochs = 15\nsteps_per_epoch = train_generator.n//train_generator.batch_size\nvalidation_steps = validation_generator.n//validation_generator.batch_size\n\n# Creating a Call Back  which reduces the Learning Rate by given factor if Val_Loss is not decreasing after \'patience\' number of Epochs.\n\nreduce_lr = ReduceLROnPlateau(monitor=\'val_loss\', factor=0.1,\n                              patience=2, min_lr=0.00001, mode=\'auto\')\n\n# Creating another Call back which saves the model_weights in .h5 format  after each epoch. Verbose option gives More Info.\n\ncheckpoint = ModelCheckpoint("trial_model_weights.h5", monitor=\'val_accuracy\',\n                             save_weights_only=True, mode=\'max\', verbose=1)\n\n# Instead of plotting using history, we are doing Live Plotting using PlotLossesKerasTF after each EPOCH \n\ncallbacks = [PlotLossesKerasTF(), checkpoint, reduce_lr]\n\n \nhistory = model.fit(\n    x=train_generator,\n    steps_per_epoch=steps_per_epoch,\n    epochs=epochs,\n    validation_data = validation_generator,\n    validation_steps = validation_steps,\n    callbacks=callbacks\n)\n\n')


#  Represent Model as JSON String

model_json = model.to_json()
with open("trial_model.json", "w") as json_file:
    json_file.write(model_json)





