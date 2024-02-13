import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from pytorch_metric_learning import samplers

### MNIST code originally from https://github.com/pytorch/examples/blob/master/mnist/main.py ###
from torchvision import datasets, transforms

from pytorch_metric_learning import distances, losses, miners, reducers, testers


### MNIST code originally from https://github.com/pytorch/examples/blob/master/mnist/main.py ###
class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.conv1 = nn.Conv2d(1, 32, 3, 1)
        self.conv2 = nn.Conv2d(32, 64, 3, 1)
        self.dropout1 = nn.Dropout2d(0.25)
        self.dropout2 = nn.Dropout2d(0.5)
        self.fc1 = nn.Linear(9216, 128)

    def forward(self, x):
        x = self.conv1(x)
        x = F.relu(x)
        x = self.conv2(x)
        x = F.relu(x)
        x = F.max_pool2d(x, 2)
        x = self.dropout1(x)
        x = torch.flatten(x, 1)
        x = self.fc1(x)
        return x

### MNIST code originally from https://github.com/pytorch/examples/blob/master/mnist/main.py ###
def train(model, loss_func, mining_func, device, train_loader, optimizer, epoch):
    model.train()
    for batch_idx, (data, labels) in enumerate(train_loader):
        data, labels = data.to(device), labels.to(device)
        optimizer.zero_grad()
        embeddings = model(data)
        indices_tuple = mining_func(embeddings, labels)
        loss = loss_func(embeddings, labels, indices_tuple)
        loss.backward()
        optimizer.step()
        if batch_idx % 20 == 0:
            print(
                "Epoch {} Iteration {}: Loss = {}, Number of mined triplets = {}".format(
                    epoch, batch_idx, loss, mining_func.num_triplets
                )
            )


### convenient function from pytorch-metric-learning ###
def get_all_embeddings(dataset, model):
    tester = testers.BaseTester()
    return tester.get_all_embeddings(dataset, model)
device = torch.device("cuda")
num_workers = 16
samples_per_class = 8
use_batch_size = True
cuda_devices = [0]
transform = transforms.Compose(
    [transforms.ToTensor(),
    transforms.Normalize((0.1307,), (0.3081,))]
)

batch_size = 32

train_dataset = datasets.MNIST(
    ".",
    train=True,
    download=True,
    transform=transform)

if len(cuda_devices) > 1:
    train_sampler = DDP_MPerClassSampler(
        dataset=train_dataset,
        labels=train_dataset.targets,
        m=samples_per_class,
        batch_size=batch_size)
else:
    train_sampler = samplers.MPerClassSampler(
        train_dataset.targets, 
        m=samples_per_class,
        length_before_new_iter=len(train_dataset),
        batch_size=batch_size if use_batch_size else None
    )

loader = torch.utils.data.DataLoader(
    train_dataset,
    batch_size=batch_size,
    drop_last=True,
    pin_memory=True,
    num_workers=num_workers,
    sampler=train_sampler
)

train_loader = torch.utils.data.DataLoader(
    train_dataset,
    batch_size=batch_size,
    shuffle=True
)

model = Net().to(device)
optimizer = optim.Adam(
    model.parameters(),
    lr=0.01)
num_epochs = 1

### pytorch-metric-learning stuff ###
distance = distances.CosineSimilarity()
reducer = reducers.ThresholdReducer(low=0)
loss_func = losses.TripletMarginLoss(
    margin=0.2,
    distance=distance,
    reducer=reducer)
mining_func = miners.TripletMarginMiner(
    margin=0.2,
    distance=distance,
    type_of_triplets="semihard"
)
for epoch in range(1, num_epochs + 1):
    train(model, loss_func, mining_func, device, train_loader, optimizer, epoch)