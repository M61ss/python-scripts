import json

import torch

from encoder import TransformerEncoder


device = 'cuda' if torch.cuda.is_available() else 'cpu'
print('Device:', device)

params = {
    'num_layers': 6,
    'num_heads': 8,
    'd_model': 16,
    'd_embedding': 128,
    'd_ff': 2048
}

print('Encoder parameters:', json.dumps(params, indent=4))

te = TransformerEncoder(
    n_blocks=params['num_layers'],
    n_heads=params['num_heads'],
    d_model=params['d_model'],
    d_embedding=params['d_embedding'],
    d_ff=params['d_ff']
)

input = torch.empty(params['d_model'], params['d_embedding'])
print('Input shape:', input.shape)

out: torch.Tensor = te(input)
print('Output shape:', out.shape)
