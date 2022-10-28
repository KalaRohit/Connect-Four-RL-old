import os
import sys
import numpy as np
import matplotlib.pyplot as plt
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim

class ConnectBot(nn.Module):
    def __init__(self, in_size = 1, h_size = 150, num_layers = 2) -> None:
        super(ConnectBot, self).__init__()
        self.input_size = in_size
        self.hidden_size = h_size
        self.num_layers = num_layers
        self.RNN_layer = torch.nn.RNN(input_size = self.input_size, hidden_size = self.hidden_size, num_layers = 2, nonlinearity='relu', batch_first = True)
        self.activation = torch.nn.Linear(1500, 7) 
        self.relu = torch.nn.ReLU()
        self.softmax = torch.nn.Softmax()

        
    
    def forward(self, x):

        batch_size = x.size(0) 
        h0 = torch.zeros(1, batch_size, self.hidden_size)
        
        RNN_output, _  = self.RNN_layer(x, h0)

        hidden_layer_output = self.hidden(RNN_output)
        final_output = self.softmax(hidden_layer_output)

        return final_output


