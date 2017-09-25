"""
:mod:`opencsv` -- open the csv file and covert the data into numpy array

 ..module:: opencsv
   :synopsis: open the ECG.csv file and convert the data into numpy array
   :license: Apache v2.0, see LICENSE for details
   :copyright: Copyright 2017 Jing-Rui Li, Inje Lee, Niranjana Shashikumar


.. moduleauthor:: Jing-Rui Li <jl714@duke.edu>

"""

import csv
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
