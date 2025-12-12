#!/bin/python3

import torch
from torchvision.datasets import MNIST
from torch.utils.data import DataLoader
from torchvision import transforms
from torch.optim import Adam
from mlp import MLP

BATCH_SIZE = 128

DEVICE = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
NUM_EPOCHS = 10
FAN_IN = 28 * 28
N_CLASSES = 10
HIDDEN_DIM = 128
LEARNING_RATE = 0.001
mlp = MLP(FAN_IN, HIDDEN_DIM, N_CLASSES).to(DEVICE)
opt = Adam(mlp.parameters(), lr=LEARNING_RATE)
loss_function = torch.nn.CrossEntropyLoss().to(DEVICE)

transform = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize((0.1307,), (0.3081,))
])

training_data = MNIST('train_data', 
                      train=True, 
                      transform=transform, 
                      download=True
                    )
dl = DataLoader(dataset=training_data,
                batch_size=BATCH_SIZE,
                drop_last=True,
                shuffle=True
            )

def compute_accuracy():
    correct = 0
    total = 0

    with torch.no_grad():
        for x, y in dl:
            x, y = x.to(DEVICE), y.to(DEVICE)
            pred = mlp(x)
            pred = torch.argmax(pred, dim=1)
            correct += torch.sum((pred == y).float())
            total += pred.shape[0]

    return correct / total
        

for i in range(NUM_EPOCHS):
    print(f"Epoch [{i}]: acc: {compute_accuracy():.3f}")
    for x, y in dl:
        x, y = x.to(DEVICE), y.to(DEVICE)
        opt.zero_grad()

        y_pred = mlp(x)
        loss = loss_function(y_pred, y)
        loss.backward()

        opt.step()

torch.save(mlp.state_dict(), 'weights.pth')
