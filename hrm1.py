# Importing dependencies
from opencsv import opencsv
from find_max_peaks import find_max_peaks
from inst_hr import inst_hr
from avg_hr import avg_hr
from avg_hr import new_hr_set
from bradtach import bradtach
import glob
import pandas as pd 

"""
This module takes in a .csv file of ECG data and will yield instantaneous
heart rates for the whole data set. It will also prompt the user to input time
in minutes, and then will output the average HR over that time. The module also
shows if user has tachycardia, bradycardia, or normal HR over the specified
period of time.
"""


def hrmonitor(filepath, output_name):
    """
    :param filepath: ECG data location
    :param output_name : Output file name
    :return: .txt file all calculated outputs
    """
    # Importing csv data
    data = opencsv(filepath)  # Update path or add file to root folder
    time = data[0]
    voltage = data[1]
    # Instantaneous heart rate that updates every 5s
    maxpeaks = find_max_peaks(voltage, time, update_time=5)
    instantaneoushr = inst_hr(maxpeaks, update_time=5)
    # Average heart rate
    # mins = float(input('Please specify a time (in min) for averaging.'))
    newhrset = new_hr_set(mins, instantaneoushr, update_time=5)
    avghr = avg_hr(newhrset[0])
    # Brady/Tachycardia
    condition = bradtach(avghr, mins)
    message = condition[1]
    # Output Information in .txt File
    HRinfo = open('{}_HR_Information.txt'.format(output_name), 'w')
    HRinfo.write("Estimated Instantaneous HR is {} beats per minute."
                 .format(instantaneoushr))
    HRinfo.write("/nEstimated Average HR is {} beats per minute in minutes/n"
                 .format(avghr, mins))
    HRinfo.write("/n{}/n".format(message))

if __name__ == "__main__":
    # Importing csv data
    # Create the list of file
    list_of_files = glob.glob('test_data/*.csv')
    mins = float(input('Please specify a time (in min) for averaging.'))
    for file_name in list_of_files:
        FI = open(file_name, 'r')
        output_name = file_name[:-4]
        hrmonitor(filepath=FI, output_name=output_name)
        FI.close()
