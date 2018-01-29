#-------------------------------------------------------------------------
#    A H M A D   M A N S O O R         ID:170947          |--10/05/2017--|
#-------------------------------------------------------------------------
#*************************************************************************
#   RIME 832 - Machine Learning Assignment 3: CNNs on CIFAR-10
#*************************************************************************
#
#----------=: import libraries :=-----------------------------------------
import keras                              # high level API for Tensorflow
from matplotlib import pyplot as plt      # to plot images, graphs...
from scipy.misc import toimage            # turn arrays into PIL images
import numpy                              # to create NumPy arrays
from time import sleep                    # for user-friendliness !
#------------------------------------------------------------------------

#----------=:  Download Data and Verify:= -------------------------------
# Download data, if not present in '~/.keras/datasets'
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# To override downloading: place 'cifar-10-batches-py.tar.gz' in 
# the directory '~/.keras/datasets' and extract it there to get the 
# following directory: '.keras/datasets/cifar-10-batches-py/' with the
# files: test_batch, data_batch_1, data_batch_2....
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
print('Please be patient, this program is computation-extensive, and may take time to load...') # depends
sleep(0.5)
print('Verifying if CIFAR 10 dataset exists, if not, it will be downloaded:')
from keras.datasets import cifar10
sleep(0.5)
# Assign variables
(X_train, y_train), (X_test, y_test) = cifar10.load_data()
sleep(0.5)
print('CIFAR-10 dataset has been loaded...')
# Plot a grid of 3x3 images to preview data
for i in range(0, 9):
	plt.subplot(330 + 1 + i)
	plt.imshow(toimage(X_train[i]))
	
sleep(0.5)
print('Verifying data, by plotting images from the dataset..')
plt.show()

#----------=:  Initialization  :=-------------------------------------

# Using high-level builder API (Keras) to import layer structures
from keras.models import Sequential
from keras.layers.convolutional import Conv2D
from keras.layers.convolutional import MaxPooling2D
from keras.layers import Dense
from keras.layers import Dropout
from keras.layers import Flatten
from keras.constraints import maxnorm
from keras.optimizers import SGD
from keras.utils import np_utils
from keras import backend as K
K.set_image_dim_ordering('th')
#----------------------------------------------------------------------
# Assign a constant to the random number seed.
seed = 7
numpy.random.seed(seed)
#-----------------------------------------------------------------------
# Load the data, onto the respective variables :)
(X_train, y_train), (X_test, y_test) = cifar10.load_data()
#-----------------------------------------------------------------------	
# Normalize the pixel intensity values from 0-255 to 0.0-1.0
X_train = X_train.astype('float32')
X_test = X_test.astype('float32')
X_train = X_train / 255.0
X_test = X_test / 255.0
#-----------------------------------------------------------------------
# Assign variables to the labels: One-Hot Encoding
y_train = np_utils.to_categorical(y_train)
y_test = np_utils.to_categorical(y_test)
num_classes = y_test.shape[1]

#=======================================================================

#----------=:  Network Construction  :=---------------------------------

# Create the model using Keras:
model = Sequential()
model.add(Conv2D(32, (3, 3), input_shape=(3, 32, 32), activation='relu', padding='same'))
model.add(Dropout(0.2))
model.add(Conv2D(32, (3, 3), activation='relu', padding='same'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Conv2D(64, (3, 3), activation='relu', padding='same'))
model.add(Dropout(0.2))
model.add(Conv2D(64, (3, 3), activation='relu', padding='same'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Conv2D(128, (3, 3), activation='relu', padding='same'))
model.add(Dropout(0.2))
model.add(Conv2D(128, (3, 3), activation='relu', padding='same'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Flatten())
model.add(Dropout(0.2))
model.add(Dense(1024, activation='relu', kernel_constraint=maxnorm(3)))
model.add(Dropout(0.2))
model.add(Dense(512, activation='relu', kernel_constraint=maxnorm(3)))
model.add(Dropout(0.2))
model.add(Dense(num_classes, activation='softmax'))
# Assign parameters and compile model
epochs = 20
lrate = 0.01
decay = lrate/epochs
sgd = SGD(lr=lrate, momentum=0.9, decay=decay, nesterov=False)
model.compile(loss='categorical_crossentropy', optimizer=sgd, metrics=['accuracy'])
print('The network model has been compiled, this is what the network looks like:')
print(model.summary())
#-------------------------------------------------------------------------
# Fiting the model and saving the data to 'history' variable
print('Now fitting the model with the training data, using test for validation..')
history = model.fit(X_train, y_train, validation_data=(X_test, y_test), epochs=epochs, batch_size=32)
# Final evaluation of the model
scores = model.evaluate(X_test, y_test, verbose=0)
print("Accuracy: %.2f%%" % (scores[1]*100))
# Print all data in history and plot data
print('Now displaying network history')
print(history.history.keys())
# summarize history for accuracy
plt.figure
print('Plotting Training/Validation Accuracy and Loss')
plt.subplot(321)
plt.plot(history.history['acc'])
plt.plot(history.history['val_acc'])
plt.title('CIFAR-10: model accuracy')
plt.ylabel('accuracy')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')

# summarize history for loss
plt.subplot(322)
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('CIFAR-10: model loss')
plt.ylabel('loss')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')

plt.text(0, 0, r'RIME 832: Assignment 3 | Submission by Ahmad')
plt.grid(True)
plt.show()
#------------------------------------------------------------------------
# plot a keras model and save a file
from keras.utils import plot_model
plot_model(model, to_file='model.png', show_layer_names=True)
#-------------------------------------------------------------------------
# https://github.com/blackvitriol                                     -A7
#-------------------------------------------------------------------------
#******************************* ~ fin ~ *********************************
