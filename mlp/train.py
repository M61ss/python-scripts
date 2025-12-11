#!/bin/python3

from torchvision.datasets import MNIST
from torch.utils.data import Dataset, DataLoader
from torchvision import transforms

BATCH_SIZE = 128

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