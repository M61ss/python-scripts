import torch
import torch.nn as nn


class MultiHeadAttetion(nn.Module):
    def __init__(self, num_heads: int, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.num_heads = num_heads


class TransformerEncoderBlock(nn.Module):
    def __init__(self, num_heads: int, d_model: int, fc_hidden_dim: int = 512, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.num_heads = num_heads
        self.d_model = d_model
        self.fc_hidden_dim = fc_hidden_dim

        self.mha = MultiHeadAttetion(num_heads)
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
