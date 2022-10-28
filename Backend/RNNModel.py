import os
import sys
import numpy as np
import matplotlib.pyplot as plt
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torch.utils.data import Dataset

class ConnectBot(nn.Module):
    def __init__(self) -> None:
        super(ConnectBot, self).__init__()

        self.block1 = torch.nn.Sequential(
            torch.nn.RNN(input_size = 1, hidden_size = 20, num_layers = 1, nonlinearity='relu', batch_first = True)
        )

        
    
    def forward(self, x):
        x = self.block1(x)
        return x


