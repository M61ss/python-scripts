import torch
import torch.nn as nn

from attention import MultiHeadSelfAttetion
from ff import FF


class TransformerEncoderBlock(nn.Module):
    def __init__(self, num_heads: int, d_model: int, d_ff: int):
        super(TransformerEncoderBlock, self).__init__()
        self.num_heads = num_heads
        self.d_model = d_model
        self.d_ff = d_ff

        self.mha = MultiHeadSelfAttetion(num_heads, d_model)
        self.ln_1 = nn.LayerNorm(d_model)
        self.fc = FF(d_model, d_ff)
        self.ln_2 = nn.LayerNorm(d_model)

    def forward(self, X: torch.Tensor):
        out = self.mha(X)
        X = self.ln_1(out + X)
        out = self.fc(X)
        return self.ln_2(out + X)


class TransformerEncoder(nn.Module):
    def __init__(self, n_blocks: int, n_heads: int, d_model: int, d_ff: int = 1024):
        super(TransformerEncoder, self).__init__()
        self.n_blocks = n_blocks
        self.n_heads = n_heads
        self.d_model = d_model
        self.d_ff = d_ff

        self.cls = nn.Parameter(torch.zeros(1, d_model))
        self.net = nn.Sequential(
            [ 
                TransformerEncoderBlock(n_heads, d_model, d_ff) for _ in range(n_blocks) 
            ]
        )

    def forward(self, X: torch.Tensor):
        X = torch.cat([self.cls, X], dim=0)
        return self.net(X)
