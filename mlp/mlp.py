import torch
import torch.nn as nn

torch.cuda.is_available()

class MLP(nn.Module):
    """
    Works with: 28x28 grayscale images
    """
    def __init__(self, input_dim : int, hidden_dim : int, output_dim : int):
        super(MLP, self).__init__()

        self.in_dim = input_dim
        self.h_dim = hidden_dim
        self.out_dim = output_dim

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
