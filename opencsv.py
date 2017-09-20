import csv
import pandas as pd
import numpy as np


# Function to open and covert a csv file to a list of dictionaries

# Function to open and covert a csv file to a list of dictionaries


def opencsv(variables_file):
    # Open variable-based csv, iteratre over the rows and columns
    # "rb"= read the file in binary mode
    data = np.loadtxt(variables_file, dtype='float', delimiter=",", skiprows=1)
    time = np.array(data[:, 0])
    voltage = np.array(data[:, 1])
    return time, voltage

