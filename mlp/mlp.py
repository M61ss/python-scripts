import torch
import torch.nn as nn


class MLP(nn.Module):
    def __init__(self, in_dim: int, h_dim: int, out_dim: int, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.in_dim     = in_dim
        self.h_dim      = h_dim
        self.out_dim    = out_dim

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

    def forward(self, X: torch.Tensor):
        return self.net(X)
