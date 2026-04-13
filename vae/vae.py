import torch
import torch.nn as nn


class Encoder(nn.Module):
    def __init__(self, in_dim: int, out_dim: int, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.in_dim = in_dim
        self.out_dim = out_dim
        self.reduction_step = torch.abs(out_dim - in_dim) / 3

        self.net = nn.Sequential(
            nn.Linear(self.in_dim, self.in_dim - self.reduction_step),
            nn.LeakyReLU(),
            nn.Linear(self.in_dim - self.reduction_step, self.in_dim - 2 * self.reduction_step),
            nn.LeakyReLU(),
            nn.Linear(self.in_dim - 2 * self.reduction_step, self.out_dim)
        )


    def forward(self, X: torch.Tensor):
        return self.net(X)
    

class Decoder(nn.Module):
    def __init__(self, in_dim: int, out_dim: int, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.in_dim = in_dim
        self.out_dim = out_dim
        self.expansion_step = torch.abs(in_dim - out_dim) / 3

        self.net = nn.Sequential(
            nn.Linear(self.in_dim, self.in_dim + self.expansion_step),
            nn.LeakyReLU(),
            nn.Linear(self.in_dim + self.expansion_step, self.in_dim + 2 * self.expansion_step),
            nn.LeakyReLU(),
            nn.Linear(self.in_dim + 2 * self.expansion_step, self.out_dim)
        )

    
    def forward(self, X: torch.Tensor):
        return self.net(X)


class VariationalAutoencoder(nn.Module):
    def __init__(self, in_dim: int, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.in_dim = in_dim

    
    def forward(self, X: torch.Tensor):
        pass