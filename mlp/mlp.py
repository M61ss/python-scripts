import torch
import torch.nn as nn

FAN_IN = 28 * 28
N_CLASSES = 10
HIDDEN_DIM = 128

class MLP(nn.Module):
    def __init__(self):
        super(MLP, self).__init__()

        self.in_dim = FAN_IN
        self.h_dim = HIDDEN_DIM
        self.out_dim = N_CLASSES

        self.net = nn.Sequential(
            nn.Linear(self.in_dim, self.h_dim),
            nn.ReLU(),
            nn.Linear(self.h_dim, self.h_dim),
            nn.ReLU(),
            nn.Linear(self.h_dim, self.h_dim),
            nn.ReLU(),
            nn.Linear(self.h_dim, self.h_dim),
            nn.ReLU(),
            nn.Linear(self.h_dim, self.out_dim),
        )

    def forward(self, x : torch.Tensor):
        x = torch.flatten(x, 1)
        return self.net(x)
