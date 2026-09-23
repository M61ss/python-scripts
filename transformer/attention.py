import torch
import torch.nn as nn


class SelfAttention(nn.Module):
    def __init__(self, d_k: int, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.d_model = d_k

        self.qW = nn.Linear(
            in_features=d_k,
            out_features=d_k
        )
        self.kW = nn.Linear(
            in_features=d_k,
            out_features=d_k
        )
        self.vW = nn.Linear(
            in_features=d_k,
            out_features=d_k
        )

    def forward(self, X: torch.Tensor):
        Q: torch.Tensor = self.qW(X)
        K: torch.Tensor = self.kW(X)
        V: torch.Tensor = self.vW(X)
        a: torch.Tensor = torch.softmax((Q * K.T) / self.d_qk)
        return a * V


class MultiHeadSelfAttetion(nn.Module):
    def __init__(self, num_heads: int, d_model: int, *args, **kwargs):
        super().__init__(*args, **kwargs)
        assert d_model % num_heads == 0, "Embedding dimension must be multiple of head number."

        self.num_heads = num_heads
        self.d_model = d_model
        self.d_k = self.d_model // num_heads

        self.heads = [SelfAttention(
                d_k=d_model,
            ) for _ in range(num_heads)]

    def forward(self, X: torch.Tensor):
        for head in self.heads:
            o = head(X)
            out = torch.cat([out, o], dim=0)
        return out