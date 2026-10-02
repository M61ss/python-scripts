from math import sqrt

import torch
import torch.nn as nn


class SelfAttention(nn.Module):
    def __init__(self, d_head: int):
        super(SelfAttention, self).__init__()
        self.d_model = d_head

        self.qW = nn.Linear(d_head, d_head)
        self.kW = nn.Linear(d_head, d_head)
        self.vW = nn.Linear(d_head, d_head)
        self.softmax = nn.Softmax(0)

    def forward(self, X: torch.Tensor):
        Q: torch.Tensor = self.qW(X)
        K: torch.Tensor = self.kW(X)
        V: torch.Tensor = self.vW(X)
        a: torch.Tensor = self.softmax((Q * K.T) / sqrt(self.d_model))
        return a * V


class MultiHeadSelfAttetion(nn.Module):
    def __init__(self, num_heads: int, d_model: int):
        super(MultiHeadSelfAttetion, self).__init__()
        assert d_model % num_heads == 0, "Embedding dimension must be multiple of head number."

        self.num_heads = num_heads
        self.d_model = d_model
        self.d_head = self.d_model // num_heads

        self.heads = [ SelfAttention(self.d_head) for _ in range(num_heads) ]

    def forward(self, X: torch.Tensor):
        out = torch.empty(self.d_head, 0)
        for i, head in enumerate(self.heads):
            o = head(X[:, self.d_head*i : self.d_head*i+self.d_head])
            out = torch.cat([out, o], dim=1)
        return out