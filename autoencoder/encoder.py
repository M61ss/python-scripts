import torch
import torch.nn as nn


class Encoder(nn.Module):
    def __init__(self, in_dim: int, out_dim: int, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.in_dim = in_dim
        self.out_dim = out_dim
        self.hidden_dim = torch.abs(self.in_dim - self.out_dim) / 2
        self.net = nn.Sequential(
            nn.Linear(self.in_dim, self.hidden_dim),
            nn.LeakyReLU(),
            nn.Linear(self.hidden_dim, self.out_dim)
        )

    def forward(self, X: torch.Tensor):
        return self.net(X)
