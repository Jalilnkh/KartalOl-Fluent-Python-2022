import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import datasets
from torchvision.transforms import ToTensor
from torch.utils.data import DataLoader


class Net(nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = nn.Linear(784, 50) 
        self.fc2 = nn.Linear(50, 10)

    def forward(self, x):
        x = x.view(-1, 784)
        x = torch.relu(self.fc1(x))
        x = self.fc2(x)
        return x


def train(num_epoch):
    # Define model
    model = Net()
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(), lr=0.001)
    
    # Define and load data
    train_data = datasets.MNIST(
        root="./data",
        train=True,
        download=True,
        transform=ToTensor()
    )

    train_loader = DataLoader(
        train_data,
        batch_size=64,
        shuffle=True,
        num_workers=2
    )
    for epoch in range(num_epoch):
        for inputs, labels in train_loader:
            optimizer.zero_grad()
            outputs = model(inputs)
            loss = criterion(outputs, labels)

            loss.backward()
            optimizer.step()
        print(f'Epoch [{epoch+1}/{num_epoch}], Loss: {loss.item():.4f}')


if __name__ == "__main__":
    num_epoch = 2
    train(num_epoch) 
