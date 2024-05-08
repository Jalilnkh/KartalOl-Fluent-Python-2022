import numpy as np

class LeakyReLU:
    def __call__(self, x):
        return np.where(x > 0, x, 0.01 * x)

class MSELoss:
    def __call__(self, pred, true):
        return np.mean((pred - true) ** 2)

class Layer:
    def __init__(self, input_dim, output_dim, activation):
        self.weights = np.random.randn(input_dim, output_dim) * 0.1  # Initialize weights
        self.bias = np.zeros(output_dim)
        self.activation = activation

    def forward(self, x):
        z = np.dot(x, self.weights) + self.bias
        return self.activation(z)

class NeuralNetwork:
    def __init__(self, layers, loss_fn, learning_rate):
        self.layers = layers
        self.loss_fn = loss_fn
        self.learning_rate = learning_rate

    def forward_pass(self, x):
        for layer in self.layers:
            x = layer.forward(x)
        return x

    def compute_loss(self, pred, true):
        return self.loss_fn(pred, true)

    def train(self, x, y):
        # Dummy function for training
        predictions = self.forward_pass(x)
        return self.compute_loss(predictions, y)

def generate_syn_data(num_samples, img_dim1, img_dim2, num_classes):
    X_train = np.random.rand(int(0.9*num_samples), img_dim1 * img_dim2)  # Generate random flat images
    y_train = np.random.randint(0, num_classes, size=(int(0.9*num_samples), 1))  # Random labels
    X_test = np.random.rand(int(0.1*num_samples), img_dim1 * img_dim2)  # Generate random flat images
    y_test = np.random.randint(0, num_classes, size=(int(0.1*num_samples), 1))  # Random labels
    return X_train, y_train, X_test, y_test

# Correct the network architecture
net = NeuralNetwork([
    Layer(784, 10, LeakyReLU()),  # Corrected input dimension
    Layer(10, 4, LeakyReLU()),
    Layer(4, 10, LeakyReLU()),
    Layer(10, 4, LeakyReLU()),
    Layer(4, 10, LeakyReLU()),
], MSELoss(), 0.001)

# Generate synthetic data
X_train, y_train, X_test, y_test = generate_syn_data(1000, 28, 28, 10)  # Correct dimensions and number of classes

epochs = 20
batch_size = 100  # Assuming batch processing

for epoch in range(epochs):
    loss = 0
    e_loss = 0
    # Iterate over batches
    for i in range(0, 900, batch_size):
        batch_X = X_train[i:i+batch_size]
        batch_y = y_train[i:i+batch_size]
        loss += net.train(batch_X, batch_y)

    # Evaluation (simple example, without proper data separation)
    pred = net.forward_pass(X_test)
    e_loss = net.compute_loss(pred, y_test)

    print(f"Epoch {epoch+1}, Training Loss: {loss / (100 / batch_size)}")
    print(f"Epoch {epoch+1}, Evaluated Loss: {e_loss / 100}")
