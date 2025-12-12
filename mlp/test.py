#!/bin/python3

import torch
from torch.utils.data import DataLoader
from torchvision.transforms import transforms
from torchvision.datasets import MNIST
from mlp import MLP

BATCH_SIZE = 128
DEVICE = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

NUM_EPOCHS = 10
LEARNING_RATE = 0.001
mlp = MLP().to(DEVICE)
mlp.load_state_dict(torch.load('weights.pth'))

transform = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize((0.1307,), (0.3081,))
])

test_data = MNIST(
    'test_data',
    transform=transform,
    train=False,
    download=True
)

dl = DataLoader(
    dataset=test_data,
    batch_size=BATCH_SIZE,
    shuffle=True,
    drop_last=True
)

correct = 0
total = 0

for x, y in dl:
    x, y = x.to(DEVICE), y.to(DEVICE)
    pred = mlp(x)
    pred = torch.argmax(pred, dim=1)
    correct += torch.sum(pred == y)
    total += pred.shape[0]

print(f"Test accuracy: {correct / total:.3f}")