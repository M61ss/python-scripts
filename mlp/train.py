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
FAN_OUT = 10
HIDDEN_DIM = 128
LEARNING_RATE = 0.001
mlp = MLP(FAN_IN, HIDDEN_DIM, FAN_OUT)
opt = Adam(mlp.parameters(), lr=LEARNING_RATE)
loss_function = torch.nn.CrossEntropyLoss().to(DEVICE)

transform = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize((0.1307,), (0.3081,))
])

training_data = MNIST('data', 
                      train=True, 
                      transform=transform, 
                      download=True
                    )
dl = DataLoader(dataset=training_data,
                batch_size=BATCH_SIZE,
                num_workers=0,
                drop_last=True,
                shuffle=True
            )

for i in range(NUM_EPOCHS):
    for x, y in dl:
        x, y = x.to(DEVICE), y.to(DEVICE)
        opt.zero_grad()

        y_pred = mlp(x)
        loss = loss_function(y_pred, y)
        loss.backward()

        opt.step()
