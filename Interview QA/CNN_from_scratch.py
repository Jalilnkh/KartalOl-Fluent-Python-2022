

import numpy as np
from cnn_classes import Conv, MaxPool, Softmax
from keras.datasets import mnist

# Load data
(train_images, train_labels), (test_X, test_y) = mnist.load_data()

# Define Model
class Model:
    def __init__(self):
        self.conv = Conv(8)
        self.pool = MaxPool()
        self.softmax = Softmax(13 * 13 * 8, 10)  # adjust the size as per your architecture details

    def forward(self, image, label):
        # Normalize the image
        out = self.conv.forward((image / 255) - 0.5)
        out = self.pool.forward(out)
        out = self.softmax.forward(out)
        # Calculate cross-entropy loss and accuracy
        loss = -np.log(out[label])
        acc = 1 if np.argmax(out) == label else 0

        return out, loss, acc

    def train(self, im, label, lr=0.005):
        # Forward pass
        out, loss, acc = self.forward(im, label)
        # Start of the backward pass
        gradient = np.zeros(10)
        gradient[label] = -1 / out[label]
        # Backpropagation
        gradient = self.softmax.backprop(gradient, lr)
        gradient = self.pool.backprop(gradient)
        gradient = self.conv.backprop(gradient, lr)

        return loss, acc

    def evaluate(self, test_images, test_labels):
        total_loss = 0
        total_correct = 0

        for i, (im, label) in enumerate(zip(test_images, test_labels)):
            _, loss, acc = self.forward(im, label)
            total_loss += loss
            total_correct += acc

        average_loss = total_loss / len(test_images)
        accuracy = total_correct / len(test_images)
        return average_loss, accuracy

model = Model()

# Training loop
for epoch in range(3):
    print('----EPOCH %d ---' % (epoch + 1))
    permutation = np.random.permutation(len(train_images))
    shuffled_train_images = train_images[permutation]
    shuffled_train_labels = train_labels[permutation]

    for i in range(len(shuffled_train_images)):
        loss, acc = model.train(shuffled_train_images[i], shuffled_train_labels[i])
        if i % 100 == 99:
            print(f'[Step {i + 1}] Loss: {loss:.3f} | Accuracy: {acc * 100:.2f}%')

    # Evaluation
    avg_loss, accuracy = model.evaluate(test_X, test_y)
    print(f'Evaluation - Loss: {avg_loss:.3f}, Accuracy: {accuracy * 100:.2f}%')
