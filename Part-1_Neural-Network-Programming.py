import torch
import numpy as np
import torchvision
import torchvision.transforms as transforms

train_set = torchvision.datasets.FashionMNIST(
    root="./data",
    train=True,
    download=False,
    transform=transforms.Compose([
        transforms.ToTensor()
    ])
)

train_loader = torch.utils.data.DataLoader(train_set, batch_size=10)

print(train_loader)

print("haaaaalo")