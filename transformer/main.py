import torch
from .encoder import TransformerEncoder


device = 'cuda' if torch.cuda.is_available() else 'cpu'
print('Device:', device)

N_BLOCKS = 6
N_HEADS = 8
D_MODEL = 128
D_FF = 512


te = TransformerEncoder(
    n_blocks=N_BLOCKS,
    n_heads=N_HEADS,
    d_model=D_MODEL,
    d_ff=D_FF
).to(device)

