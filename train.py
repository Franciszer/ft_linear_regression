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

def model(X, w, b):
    # model
    return X * w + b

def squared_loss(y_hat, y):
    # loss fuction
    return (y_hat - y)**2 / 2

def sgd(params, lr):
    # stochastic gradient descent
    with torch.no_grad():
        for param in params:
            param -= lr * param.grad / 24
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
    X, y = inputs.values.astype(float) , outputs.values.astype(float)

    t0, t1 = [0.0, 0.0]

    lr = 1e-7
    sc_t0 = 1e5
    sc_t1 = 1e-5
    num_epochs = 10000
    m = y.size

    for epoch in range(num_epochs):
        preds = model(X, t1, t0)

        loss = preds - y
        cost0 = lr * np.sum(loss) / m
        cost1 = lr * np.sum(loss * X) / m
        t0 -= sc_t0 * cost0
        t1 -= sc_t1 * cost1
        # print(f'epoch {epoch} loss {np.sum(preds - y)} t1 {t1} t0 {t0}')

    # print(f'prediction on training data:\n{torch.matmul(X, w) + b}')
    print(f'epoch {epoch} loss {np.sum(preds - y)} t1 {t1} t0 {t0}')
    # print(f'loss {results.mean():f}')
    write_parameters('parameters.txt', t1, t0)
# # See PyCharm help at https://www.jetbrains.com/help/pycharm/
