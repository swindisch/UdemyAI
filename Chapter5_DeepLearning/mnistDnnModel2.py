from keras.layers import *
from keras.models import *
from keras.optimizers import *

from mnistData import *


mnist_data = MNIST()
x_train, y_train = mnist_data.get_train_set()
x_test, y_test = mnist_data.get_test_set()

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

# Train the DNN
lr = 0.001 # (0, 1)
optimizer = Adam(lr=lr)
model.compile(
    loss="categorical_crossentropy",
    optimizer=optimizer,
    metrics=["accuracy"])
model.fit(
    x_train,
    y_train,
    verbose=1,
    batch_size=128,
    epochs=10)

# Test the DNN
acc = model.evaluate(x_test, y_test, verbose=0)
print("Test accuracy: ", acc)
