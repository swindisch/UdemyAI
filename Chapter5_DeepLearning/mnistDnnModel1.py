# Imports
from keras.models import *
from keras.layers import *
from keras.optimizers import *

# Load MNIST dataset
from mnistData import *
mnist_data = MNIST()

num_features = 784
num_classes = 10

# Define the DNN
model = Sequential()
# Hidden Layer 1
model.add(Dense(512, input_shape=(num_features,)))
model.add(Activation("relu"))
# Hidden Layer 2
model.add(Dense(512))
model.add(Activation("relu"))
# Output Layer
model.add(Dense(num_classes))
model.add(Activation("softmax"))

# Print the DNN layers
model.summary()