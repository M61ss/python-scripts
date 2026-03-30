import torch
import torch.nn as nn


class MLP(nn.Module):
    """
    Works with 28 * 28 images
    """
    def __init__(self, fan_in, hidden_dim, n_classes, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.in_dim = fan_in
        self.h_dim = hidden_dim
        self.out_dim = n_classes

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
