import torch

from encoder import TransformerEncoder


device = 'cuda' if torch.cuda.is_available() else 'cpu'
print('Device:', device)

params = {
    'num_layers': 6,
    'num_heads': 8,
    'd_model': 128,
    'd_ff': 2048
}

print('Encoder parameters:', params)

te = TransformerEncoder(
    n_blocks=params['num_layers'],
    n_heads=params['num_heads'],
    d_model=params['d_model'],
    d_ff=params['d_ff']
).to(device)

input = torch.empty(16, params['d_model']).to(device)
print('Input shape:', input.shape)

out: torch.Tensor = te(input)
print(out.shape)

assert input.shape == out.shape, "Input and output shapes mismatch."
