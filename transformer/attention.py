import torch
import torch.nn as nn


class SelfAttention(nn.Module):
    def __init__(self, d_head: int):
        super(SelfAttention, self).__init__()
        self.d_model = d_head

        self.qW = nn.Linear(d_head, d_head)
        self.kW = nn.Linear(d_head, d_head)
        self.vW = nn.Linear(d_head, d_head)

    def forward(self, X: torch.Tensor):
        Q: torch.Tensor = self.qW(X)
        K: torch.Tensor = self.kW(X)
        V: torch.Tensor = self.vW(X)
        a: torch.Tensor = torch.softmax((Q * K.T) / torch.sqrt(self.d_model))
        return a * V


class MultiHeadSelfAttetion(nn.Module):
    def __init__(self, num_heads: int, d_model: int):
        super(MultiHeadSelfAttetion, self).__init__()
        assert d_model % num_heads == 0, "Embedding dimension must be multiple of head number."

        self.num_heads = num_heads
        self.d_model = d_model
        self.d_head = self.d_model // num_heads

        self.heads = [SelfAttention(self.d_head) for _ in range(num_heads)]

    def forward(self, X: torch.Tensor):
        for head in self.heads:
            o = head(X)
            out = torch.cat([out, o], dim=0)
        return out