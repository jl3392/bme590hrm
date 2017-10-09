# Importing dependencies
from opencsv import opencsv
from find_max_peaks import find_max_peaks
from inst_hr import inst_hr
from avg_hr import avg_hr
from avg_hr import new_hr_set
from bradtach import bradtach
from glob import glob

"""
This module takes in a .csv file of ECG data and will yield instantaneous
heart rates for the whole data set. It will also prompt the user to input time
in minutes, and then will output the average HR over that time. The module also
shows if user has tachycardia, bradycardia, or normal HR over the specified
period of time.
"""


def hrmonitor(filepath):
    """
    :param filepath: ECG data location
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
    mins = float(input('Please specify a time (in min) for averaging.'))
    newHRset = new_hr_set(mins, instantaneoushr, update_time=5)
    avgHR = avg_hr(newHRset[0], newHRset[1])
    # Brady/Tachycardia
    condition = bradtach(avgHR, mins)
    message = condition[1]
    # Output Information in .txt File
    HRinfo = open('HR_Information.txt', 'w')
    HRinfo.write("Estimated Instantaneous HR is {} beats per minute."
                 .format(instantaneoushr))
    HRinfo.write("/nEstimated Average HR is {} beats per minute in minutes/n"
                 .format(avgHR, mins))
    HRinfo.write("/n{}/n".format(message))

if __name__ == "__main__":
    # Importing csv data
    # Create the list of file
    list_of_files = glob.glob('Data/*.csv')
    for file_name in list_of_files:
        FI = open(file_name, 'r')
        for line in FI:
            extime = file_name[0]
            exvoltage = file_name[1]
        FI.close()

    # exampledata = opencsv('Data/ecg_data.csv')
    # extime = exampledata[0]
    # exvoltage = exampledata[1]

    # Instantaneous heart rate updates every 5s
    exmaxpeaks = find_max_peaks(exvoltage, extime, update_time=5)
    exinstantaneoushr = inst_hr(exmaxpeaks, update_time=5)

    # Average heart rate
    exmins = float(input('Please specify a time (in min) for averaging.'))
    exnewHRset = new_hr_set(exmins, exinstantaneoushr, update_time=5)
    exavgHR = avg_hr(exnewHRset[0], exnewHRset[1])

    # Brady/Tachycardia
    excondition = bradtach(exavgHR, exmins)
    exmessage = excondition[1]

    print("Estimated Instantaneous HR is {} beats per minute."
          .format(exinstantaneoushr))
    print("Estimated Average HR is {} beats per minute in minutes"
          .format(exavgHR, exmins))
    print("{}".format(exmessage))
