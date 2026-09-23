import torch
import torch.nn as nn


class FF(nn.Module):
    def __init__(self, d_model: int, hidden_dim: int, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.hidden_dim = hidden_dim

        self.ffn = nn.Sequential(
            nn.Linear(
                in_features=d_model,
                out_features=hidden_dim
            ),
            nn.LeakyReLU(),
            nn.Linear(
                in_features=hidden_dim,
                out_features=d_model
            )
        )

    def forward(self, X: torch.Tensor):
        return self.ffn(X)