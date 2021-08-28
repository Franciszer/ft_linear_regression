# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import torch
import matplotlib

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.

# def predict(w, b):

def parse_parameters(path):
    text_file = open(path, 'r')
    file_data = text_file.read()
    params = map(int, file_data.split(' '))
    return params

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    w, b = parse_parameters('./parameters.txt')
    print(f'w: {w}  b:{b}')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
