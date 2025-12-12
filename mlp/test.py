from torch.utils.data import DataLoader
from torchvision.transforms import transforms
from torchvision.datasets import MNIST

BATCH_SIZE = 128

transform = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize((0.1307,), (0.3081,))
])

test_data = MNIST(
    'test_data',
    transform=transform,
    train=False,
    download=True
)

dl = DataLoader(
    dataset=test_data,
    batch_size=BATCH_SIZE,
    shuffle=True,
    drop_last=True
)