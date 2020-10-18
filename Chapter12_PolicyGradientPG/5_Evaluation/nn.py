from tensorflow.keras.layers import Activation
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import Input
from tensorflow.keras.models import Model
from tensorflow.keras.optimizers import Adam


class NN(Model):
    def __init__(self, state_shape, num_actions, lr):
        super(NN, self).__init__()
        self.state_shape = state_shape
        self.num_actions = num_actions
        self.lr = lr

        state = Input(shape=(state_shape,))
        x = Dense(24)(state)
        x = Activation("relu")(x)
        x = Dense(self.num_actions)(x)
        out = Activation("softmax")(x)
        self.model = Model(inputs=state, outputs=out)
        self.model.compile(loss="categorical_crossentropy", optimizer=Adam(learning_rate=self.lr))

    def train(self, states, q_values):
        self.model.fit(states, q_values, verbose=0)

    def predict(self, state):
        return self.model.predict(state)

    def update_model(self, other_model):
        self.model.set_weights(other_model.get_weights())

    def load_model(self, path):
        self.model.load_weights(path)

    def save_model(self, path):
        self.model.save_weights(path)
