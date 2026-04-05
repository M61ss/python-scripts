import torch
from torchvision.datasets import MNIST
from torch.utils.data import DataLoader
from torchvision import transforms
from torch.optim import Adam
from mlp import MLP

DEVICE = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

def compute_accuracy():
    correct = 0
    total = 0

    with torch.no_grad():
        for x, y in dl:
            x, y = x.to(DEVICE), y.to(DEVICE)
            x = torch.flatten(x, 1)
            pred = mlp(x)
            pred = torch.argmax(pred, dim=1)
            correct += torch.sum(pred == y)
            total += pred.shape[0]

    return correct / total


BATCH_SIZE = 128

transform = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize((0.1307,), (0.3081,))
])

training_data = MNIST('train_data', 
                      train=True, 
                      transform=transform, 
                      download=True
                    )
dl = DataLoader(dataset=training_data,
                batch_size=BATCH_SIZE,
                drop_last=True,
                shuffle=True
            )


INPUT_DIM       = 28 * 28
HIDDEN_DIM      = 256
OUTPUT_DIM      = 10
NUM_EPOCHS      = 3
LEARNING_RATE   = 0.001

mlp = MLP(
    in_dim=INPUT_DIM,
    h_dim=HIDDEN_DIM,
    out_dim=OUTPUT_DIM
).to(DEVICE)

opt = Adam(
    mlp.parameters(),
    lr=LEARNING_RATE
)

loss_function = torch.nn.CrossEntropyLoss().to(DEVICE)   

for i in range(NUM_EPOCHS):
    print(f'Epoch [{i}]:')
    for x, y in dl:
        x, y = x.to(DEVICE), y.to(DEVICE)
        opt.zero_grad()

        x = torch.flatten(x, 1)
        y_pred = mlp(x)
        loss = loss_function(y_pred, y)
        loss.backward()

        opt.step()
    print(f' - Accuracy: {compute_accuracy():.3f}')
    print('-' * 20)

print('Saving model weights to "weights.pth"...')
torch.save(mlp.state_dict(), 'weights.pth')
