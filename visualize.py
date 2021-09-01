# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import torch
import matplotlib
import os
import pandas
import torch
import matplotlib.pyplot as plt
import numpy as np
import pandas
import torch
import matplotlib.pyplot as plt
import numpy as np
import sys

def parse_data(data_path):
    with open(data_path, 'r') as f:
        data = pandas.read_csv(f)
        return data
    # return data

def parse_parameters(path):
    text_file = open(path, 'r')
    file_data = text_file.read()
    text_file.close()
    params = map(float, file_data.split(' '))
    return params


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    # get weight and bias
    parameters_file = "./parameters.txt"
    try:
        w, b = parse_parameters(parameters_file)
    except FileNotFoundError:
        print(f"Could not find {parameters_file}, please run the training program", file=sys.stderr)
        exit(2)

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

    plt.scatter(X, y)
    xx = np.linspace(0, torch.max(X))
    yy = xx * w + b
    plt.plot(xx, yy)
    plt.show()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
