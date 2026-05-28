from encoder import TransformerEncoder


N_BLOCKS = 6
N_HEADS = 8
D_MODEL = 128
D_QK = 32
D_V = 64
FC_HIDDEN_DIM = 512


te = TransformerEncoder(
    n_blocks=N_BLOCKS,
    n_heads=N_HEADS,
    d_model=D_MODEL,
    d_qk=D_QK,
    d_v=D_V,
    fc_hidden_dim=FC_HIDDEN_DIM
)