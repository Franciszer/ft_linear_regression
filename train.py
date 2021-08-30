# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import random

import torch
import matplotlib
import os
import pandas
import torch
import numpy as np


def write_parameters(path, w, b):
    text_file = open(path, 'w')
    text_file.write(f'{w} {b}')
    text_file.close()


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


def parse_data(data_path):
    with open(data_path, 'r') as f:
        data = pandas.read_csv(f)
        return data
    # return data

def linreg(X, w, b):
    # model
    return torch.matmul(X, w) + b

def squared_loss(y_hat, y):
    # loss fuction
    return (y_hat - y)**2 / 2

def sgd(params, lr, batch_size):
    # stochastic gradient descent
    with torch.no_grad():
        for param in params:
            prd = param.grad / batch_size
            param -= lr * prd
            param.grad.zero_()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    csv_path = './data/data.csv'
    try:
        data = parse_data(csv_path)
    except FileNotFoundError:
        print(f"could not find {csv_path}")
        exit(1)

    # dividing the data between inputs and outputs
    inputs, outputs = data.iloc[:, 0], data.iloc[:, 1]

    # converting it to tensor format
    X, y = torch.tensor(inputs.values, dtype=float), torch.tensor(outputs.values, dtype=float)
    X = X.reshape(24, 1)

    w = torch.normal(0, 0.01, size=(1, 1), requires_grad=True, dtype=float)
    b = torch.normal(0, 0.01, size=(1, 1), requires_grad=True, dtype=float)

    lr = 1e-12
    num_epochs = 100
    net = linreg
    loss = squared_loss
    batch_size = 24

    for epoch in range(num_epochs):
        preds = net(X, w, b)
        l = loss(preds, y)
        # Compute gradient on l with respect to w, b
        lsum = l.sum()
        lsum.backward()
        sgd([w, b], lr, 24)
        results = loss(net(X, w, b), y)
        print(f'epoch {epoch} loss {results.mean():f} w {w.detach().numpy()[0][0]} {b.detach().numpy()[0][0]}')

    results = loss(net(X, w, b), y)
    # print(f'prediction on training data:\n{torch.matmul(X, w) + b}')
    print(f'w {w.detach().numpy()[0][0]}  b {b.detach().numpy()[0][0]}')
    # print(f'loss {results.mean():f}')
    write_parameters('parameters.txt', w.detach().numpy()[0][0], b.detach().numpy()[0][0])
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
