import torch
import torch.nn as nn


class SelfAttention(nn.Module):
    def __init__(self, d_model: int, d_qk: int, d_v: int, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.d_model = d_model
        self.d_qk = d_qk
        self.d_v = d_v

        self.qW = nn.Linear(d_model, d_qk)
        self.kW = nn.Linear(d_model, d_qk)
        self.vW = nn.Linear(d_model, d_v)


    def forward(self, X: torch.Tensor):
        Q: torch.Tensor = self.qW(X)
        K: torch.Tensor = self.kW(X)
        V: torch.Tensor = self.vW(X)
        a: torch.Tensor = torch.softmax((Q * K.T) / self.d_qk)
        return a * V


class MultiHeadAttetion(nn.Module):
    def __init__(self, num_heads: int, d_model: int, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.num_heads = num_heads
        self.d_model = d_model

        self.heads = nn.ModuleList(
            [SelfAttention(d_model=d_model) for _ in range(num_heads)]
        )


    def forward(self, X: torch.Tensor):
        return self.heads(X)


class TransformerEncoderBlock(nn.Module):
    def __init__(self, num_heads: int, d_model: int, fc_hidden_dim: int = 512, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.num_heads = num_heads
        self.d_model = d_model
        self.fc_hidden_dim = fc_hidden_dim

        self.mha = MultiHeadAttetion(num_heads, d_model)
        self.ln_1 = nn.LayerNorm()
        self.fc = nn.Sequential(
            nn.Linear(in_features=d_model, out_features=512),
            nn.Linear(in_features=512, out_features=d_model)
        )
        self.ln_2 = nn.LayerNorm()

    
    def forward(self, X: torch.Tensor):
        out = self.mha(X)
        X = self.ln_1(out + X)
        out = self.fc(X)
        return self.ln_2(out + X)


class Transformer(nn.Module):
    def __init__(self, num_blocks: int, num_heads: int, d_model: int, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.num_blocks = num_blocks
        self.num_heads = num_heads
        self.d_model = d_model
        
        self.net = nn.ModuleList(
            [TransformerEncoderBlock(num_heads, d_model) for _ in range(num_blocks)]
        )


    def forward(self, X: torch.Tensor):
        pass
