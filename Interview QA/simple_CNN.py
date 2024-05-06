# This code is taken from sentdex youtube video

import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0)

def create_data(points, classes):
    X = np.zeros((points*classes, 2))
    y = np.zeros((points*classes), dtype='uint8')
    for class_number in range(classes):
        ix = range(points*class_number, points*(class_number+1))
        r = np.linspace(0.0, 1, points)
        t = np.linspace(class_number*4, (class_number+1)*4, points) + np.random.randn(points)*0.2
        X[ix] = np.c_[r*np.sin(t*2.5), r*np.cos(t*2.5)]
        y[ix] = class_number
    return X, y


class ActivationReLU:
    def forward(self, inputs):
        self.output = np.maximum(0, inputs)


class LayerDense:
    def __init__(self, n_inputs, n_neurons) -> None:
        # 0.10 to brought value to around -1 to +1
        self.wieghts = 0.10 * np.random.randn(n_inputs, n_neurons)
        self.biases = np.zeros((1, n_neurons))

    def forward(self, inputs):
        self.output = np.dot(inputs, self.wieghts) + self.biases


class Sofmax:
    def forward(self, inputs):
        exp_value = np.exp(inputs * np.max(inputs, axis=1, keepdims=True))
        probabilities = exp_value / np.sum(exp_value, axis=1, keepdims=True)
        self.output = probabilities
class Loss:
    def calculate(self, output, y):
        sample_loses = self.forward(output, y)
        data_loss = np.mean(sample_loses)
        return data_loss
    

class LossCategoricalCrossEntropy(Loss):
    def forward(self, y_pred, y_true):
        samples = len(y_pred)
        y_pred_clipped = np.clip(y_pred, 1e-7, 1-1e-7)

        if len(y_true.shape) == 1:
            correct_confidences = y_pred_clipped[range(samples), y_true]
        elif len(y_true.shape) == 2:
            correct_confidences = np.sum(y_pred_clipped*y_true, axis=1)
        
        negative_log_likelihoods = -np.log(correct_confidences)
        return negative_log_likelihoods


X, y = create_data(100, 3)


plt.scatter(X[:,0], X[:,1])
plt.show()

plt.scatter(X[:,0], X[:,1], c=y, cmap="brg")
plt.show()

layer1 = LayerDense(2, 6)
activation1 = ActivationReLU()
layer2 = LayerDense(6, 10)
activation2 = ActivationReLU()
layer3 = LayerDense(10, 3)
activation3 = Sofmax()

layer1.forward(X)
activation1.forward(layer1.output)
layer2.forward(activation1.output)
activation2.forward(layer2.output)
layer3.forward(activation2.output)
activation3.forward(layer3.output)
loss_func = LossCategoricalCrossEntropy()
loss = loss_func.calculate(activation3.output, y)
print(loss)

