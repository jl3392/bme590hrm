import numpy as np
import pandas as pd
import math


class Ecg:

    """
    Creating this class to convert raw ECG data of all types into HR data
    and clinical indication of brady-/tachycardia.
    """
    MIN_SEC = 60
    MIN_DIST = 150

    def __init__(self, csv_file=None, update_time=5,
                 brady_threshold=60, tachy_threshold=100, mins=2):
        """
        Constructor for ECG processing needs the input csv file to work on and
        time for often to update the instantaneous HR

        :param csv_file: the input file containing ECG data
        :param update_time: instantaneous HR update time in seconds
        :param brady_threshold: threshold for bradycardia in bpm
        :param tachy_threshold: threshold for tachycardia in bpm
        """
        if csv_file:
            data = pd.read_csv(csv_file, header=None)
            data.columns = ['time', 'voltage']
            voltage = pd.to_numeric(data.voltage, errors='coerce')
            time = pd.to_numeric(data.time, errors='coerce')
            voltage = voltage.fillna(methood='pad')
            time = time.fillna(method='pad')
            voltage = voltage.as_matrix()
            time = time.as_matrix()
            self.time_array = time
            self.voltage_array = voltage
            self.update_time = update_time
            self.brady_threshold = brady_threshold
            self.tachy_threshold = tachy_threshold
            self.mins = mins
        self.divided_voltage_array = np.array([])
        self.divided_time_array = np.array([])
        self.total_peaks = []
        self.avg_hr = []
        self.status = []
        self.raw_bunches = []
        
    def prep_data(self):
        """
        Method that prepares data for get_max_peaks
        :return: none
        """
        total_time = self.time_array[-1] - self.time_array[1]
        num_groups = total_time / self.update_time  # inst HR groups

        if groups < 1:
            raise ValueError("Update time is longer than signal length")
        self.divided_voltage_array = np.array_split(self.voltage_array, groups)
        self.divided_time_array = np.array_split(self.time_array, groups)
        length = len(self.voltage_array)

        if length % num_groups != 0:  # ignore last group if not equal to others
            np.delete(self.divided_voltage_array, -1)

        if isinstance(update_time,float):
            update_time =int(update_time)
        elif isinstance(update_time, str):
            print('the update time should not be a string,please fix it.')

    def get_max_peak(self):
        """
           Method that will find local maximum of an array i.e peaks

              :return total_peaks: list of all peaks detected, arranged
               into chunks based on update_time
              :rtype: list

           """
        for i in range(len(self.divided_voltage_array)):
            dump = []
            new_time_array = self.divided_time_array[i]
            new_voltage_array = self.divided_voltage_array[i]
            max_peaks = []

            mx, mn = -np.Inf, np.Inf  # tmp var to hold max, min

            for index, (x, y) in enumerate(zip(new_time_array,
                                               new_voltage_array)):
                if y > mx:  # if current value is > tmp
                    mx = y  # tmp = current
                    max_pos = x
                if y < mn:
                    mn = y

                # Look for local max
                if y < mx:
                    if mx != np.Inf:
                        if new_voltage_array[index:index + MIN_DIST].max() < mx:
                            # Found a valid peak
                            dump.append(True)
                            max_peaks.append([max_pos, mx])
                            # Setting flags to show that a peak was found
                            mn = np.Inf
                            mx = np.Inf
                            if index + MIN_DIST >= length:
                                # signal ends before end of window, no more valid peaks can be found
                                break
                            continue
                # Now, look for local min - using this search to eliminate smaller peaks that
                # are not local peaks
                # Prevents collecting the same max peak multiple times
                if y > mn:
                    if mn != -np.Inf:
                        # Found a min point
                        if new_voltage_array[index:index + MIN_DIST].min() > mn:
                            dump.append(False)
                            # Setting flags to show that min point was found
                            mn = -np.Inf
                            mx = -np.Inf # Triggering max peak finding again
                            if index + MIN_DIST >= length:
                                # signal ends before end of window, no more valid peaks can be found
                                break

            total_peaks.append(max_peaks)
            # Remove the false hit on the first value of the y_axis
            try:
                if dump[0]:
                    max_peaks.pop(0)
                del dump
            except IndexError:
                    # no peaks were found
                    print("No peaks were found")
           

    def get_inst_hr(self):
        """
           Function that calculates inst heart rate every update_time seconds
           by counting number of peaks within update_time

           :return self.raw_bunches: divided the total_peaks into custom peaks
           :rtype: nd array

           """

        num_of_peaks = []
        if isinstance(self.update_time, float):
            self.update_time = int(self.update_time)
        for i in range(len(self.total_peaks)):
            num_of_peaks.append(len(self.total_peaks[i]))
        new_array = np.array(num_of_peaks)
        inst_heart_rate = new_array / self.update_time
        self.raw_bunches = inst_heart_rate * 60

    def get_avghr(self):
        """ returns avghr

            Method gets avghr over user-specified minutes window.
            Also gives clinical indication of tachy/bradycardia,
            based on threshold values

            :return avg_hr: Avg hr
            :return status: Brady or tachycardia
        """

        user_sec = mins * self.MIN_SEC

    # Get number of groups based off of time
        if user_sec % self.update_time == 0:
            groups = int(user_sec/self.update_time)
    # Taking an extra group if user input mins is between groups
        else:
            groups = int(math.floor(user_sec/self.update_time) + 1)

        if len(self.raw_bunches) <= groups:  # if user time is > raw data
            real_bunches = self.raw_bunches
        else:
            real_bunches = self.raw_bunches[0:groups]

    # Calculating the avghr
        self.avg_hr = math.floor(sum(real_bunches)/len(real_bunches))

    # Calculating brady-/tachycardia
        if self.brady_threshold < self.avg_hr < self.tachy_threshold:
            self.status = [2, 'You have a normal average heart rate '
                              'over the period of {} minutes'.format(self.mins)]
        elif self.avg_hr >= self.tachy_threshold:
            self.status = [1, 'You have tachycardia over the '
                              'period of {} minutes'.format(self.mins)]  # Tachy
        elif self.avg_hr <= self.brady_threshold:
            self.status = [0, 'You have bradycardia over the period of '
                              '{} minutes'.format(self.mins)]  # Brady


