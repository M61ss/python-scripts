import torch
import torch.nn as nn

from .attention import MultiHeadSelfAttetion
from .ff import FF


class TransformerEncoderBlock(nn.Module):
    def __init__(self, num_heads: int, d_model: int, d_ff: int = 512, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.num_heads = num_heads
        self.d_model = d_model
        self.d_ff = d_ff

        self.mha = MultiHeadSelfAttetion(
            num_heads=num_heads,
            d_model=d_model
        )
        self.ln_1 = nn.LayerNorm()
        self.fc = FF(
            d_model=d_model,
            hidden_dim=d_ff
        )
        self.ln_2 = nn.LayerNorm()

    def forward(self, X: torch.Tensor):
        out = self.mha(X)
        X = self.ln_1(out + X)
        out = self.fc(X)
        return self.ln_2(out + X)


class TransformerEncoder(nn.Module):
    def __init__(self, n_blocks: int, n_heads: int, out_dim: int, d_model: int, d_ff: int = 512, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.n_blocks = n_blocks
        self.n_heads = n_heads
        self.d_model = d_model
        self.d_ff = d_ff
        self.out_dim = out_dim

        self.cls = nn.Parameter(torch.zeros(1, d_model))
        self.net = nn.Sequential(
            [TransformerEncoderBlock(
                num_heads=n_heads,
                d_model=d_model,
                d_ff=d_ff,
            ) for _ in range(n_blocks)],
            nn.Linear(
                in_features=d_model * n_blocks, 
                out_features=out_dim
            )
        )

    def forward(self, X: torch.Tensor):
        X = torch.cat([self.cls, X], dim=0)
        return self.net(X)
