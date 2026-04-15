import torch
import torch.nn as nn
from encoder import Encoder
from decoder import Decoder


class Autoencoder(nn.Module):
    def __init__(self, in_dim: int, out_dim: int, code_dim: int, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.in_dim = in_dim
        self.out_dim = out_dim
        self.code_dim = code_dim
        self.net = nn.Sequential(
            Encoder(self.in_dim, self.code_dim),
            Decoder(self.code_dim, self.out_dim)
        )

    def forward(self, X: torch.Tensor):
        return self.net(X)
