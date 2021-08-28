# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import torch
import matplotlib
import os
import pandas
import torch


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


def parse_data(data_path):
    with open(data_path, 'r') as f:
        data = pandas.read_csv(f)
        return data
    # return data

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    csv_path = './data/data.csv'
    try:
        data = parse_data(csv_path)
    except FileNotFoundError:
        print(f"could not find {csv_path}")
        exit(1)
    inputs, outputs = data.iloc[:, 0], data.iloc[:, 1]
    # print(data)
    X, y = torch.tensor(inputs.values), torch.tensor(outputs.values)
    # print("Inputs\n", torch.tensor(inputs.values))
    # print("Outputs\n", torch.tensor(outputs.values))



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
