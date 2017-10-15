import csv
import numpy as np
import pandas as pd

"""
:mod:`opencsv` -- open the csv file and covert the data into numpy array

 ..module:: opencsv
   :synopsis: open the ECG.csv file and convert the data into numpy array
   :license: Apache v2.0, see LICENSE for details
   :copyright: Copyright 2017 Jing-Rui Li, Inje Lee, Niranjana Shashikumar


.. moduleauthor:: Jing-Rui Li <jl714@duke.edu>

"""


def opencsv(variables_file):
    """return time, voltage

    This function returns the time and voltage of the ECG signal inputs

    :param variables_file: The ECG signal input file
    :type variables_file: .csv file
    :return time: time of the ECG signal
    :return voltage: voltage of the ECG signal
    :rtype time: numpy array
    :rtype voltage: numpy array

    """
    df = pd.read_csv(variables_file, header=None)
    df.columns = ['time', 'voltage']
    df.voltage.astype(float).fillna(0.00)
    df.time.astype(float).fillna(0.00)
    for i in df.voltage:
        if isinstance(i, str):
            if i == df.voltage[0]:
               df.voltage[0] = 0.0
            else:
                df.voltage[i] = df.voltage[i-1]
        elif isinstance(i, float):
            df.voltage.astype(float).fillna(df.voltage[i-1])
    for i in df.time:
        if isinstance(i, str):
            if i == df.time[0]:
                df.time[0] = 0.0
            else:
                df.time[i] = df.voltage[i-1] + df.voltage[i-1]-df.voltage[i-2]
    df = df.values
    time = df[:, 0]
    voltage = df[:, 1]
    # data = np.loadtxt(variables_file, dtype='float', delimiter=",", skiprows=1)
    # time = np.array(data[:, 0])
    # voltage = np.array(data[:, 1])
    return time, voltage
