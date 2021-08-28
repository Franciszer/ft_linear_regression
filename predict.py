# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import torch
import argparse
import sys

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
    # parser = argparse.ArgumentParser(description='Process floating point numbers')
    #
    # parser.add_argument("mileage", help="mileage of the car", type=float)
    # args = parser.parse_args()
    try:
        mileage = float(input("Please enter the mileage of the car: "))
        if mileage < 0:
            raise ValueError
    except ValueError:
        print("error: input must be a positive floating point number", file=sys.stderr)
        exit(1)

    # get weight and bias
    parameters_file = "./parameters.txt"
    try:
        w, b = parse_parameters(parameters_file)
    except FileNotFoundError:
        print(f"Could not find {parameters_file}, please run the training program", file=sys.stderr)
        exit(2)

    print(f'mileage: {mileage} w: {w}  b: {b}')
    print(f'prediction: {w * mileage + b}')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
