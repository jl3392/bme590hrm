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

    def __init__(self, data, update_time=5,
                 brady_threshold=60, tachy_threshold=100, user_sec=20):
        """
        Constructor for ECG processing needs the input file(s) to work on and
        time for how often to update the instantaneous HR

        :param csv_file: the input file containing ECG data
        :param update_time: instantaneous HR update time in seconds
        :param brady_threshold: threshold for bradycardia in bpm
        :param tachy_threshold: threshold for tachycardia in bpm
        :param user_sec: Specified averaging time over data set in seconds
        :type  csv_file: comma separated value file
        :type user_sec: float/int
        :type brady_threshold: list
        :type tachy_threshold : list
        :returns: None
        :rtype: None
        """
        if data:
            data = pd.DataFrame.from_dict(data, dtype=None)

            voltage = pd.to_numeric(data.voltage, errors='coerce')
            time = pd.to_numeric(data.time, errors='coerce')
            voltage = voltage.fillna(method='pad')
            time = time.fillna(method='pad')
            voltage = voltage.as_matrix()
            time = time.as_matrix()

            self.time_array = time
            self.voltage_array = voltage
            self.update_time = update_time
            if isinstance(self.update_time, float):
                self.update_time = int(self.update_time)
            elif isinstance(self.update_time, str):
                raise ValueError('Update time must be a number')
            self.brady_threshold = brady_threshold
            if isinstance(self.brady_threshold, float):
                self.brady_threshold = int(self.brady_threshold)
            elif isinstance(self.brady_threshold, str):
                raise ValueError('Thresholds cannot be strings or floats')
            self.tachy_threshold = tachy_threshold
            if isinstance(self.tachy_threshold, float):
                self.tachy_threshold = int(self.tachy_threshold)
            elif isinstance(self.tachy_threshold, str):
                raise ValueError('Thresholds cannot be strings or floats')
            self.user_sec = user_sec
            if isinstance(self.user_sec, float):
                self.user_sec = int(self.user_sec)
            elif isinstance(self.user_sec, str):
                raise ValueError('Averaging window must be a number in s')
        self.divided_voltage_array = np.array([])
        self.divided_time_array = np.array([])
        self.total_peaks = []
        self.avg_hr = []
        self.raw_bunches = np.zeros(len(self.time_array))  # This is a list
        self.brady = []
        self.tachy = []
        self.real_bunches = []
        self.ecg_summary ={}
        self.ecg_dict = {}
        self.total_time = None
        self.indices = []
        self.rounded_max = None
        self.data_min = None

    def prep_data(self):
        """
        Method that prepares data for get_max_peaks. Divides input data into
        groups based on update_time and ensures that they are symmetric

        :returns: none
        """

        total_time = self.time_array[-1] - self.time_array[1]
        num_groups = total_time / self.update_time  # inst HR groups

        if num_groups < 1:
            raise ValueError("Update time is longer than signal length")
        self.divided_voltage_array = np.array_split(self.voltage_array,
                                                    num_groups)  # pep8
        self.divided_time_array = np.array_split(self.time_array, num_groups)
        length = len(self.voltage_array)

        if length % num_groups != 0:  # ignore last group if ~= to others
            np.delete(self.divided_voltage_array, -1)

    def get_max_peak(self):
        """
           Method that will find local maximum of an array i.e peaks
           from the each of the divided groups provided by prep_data

            :returns: none
           """
        for i in range(len(self.divided_voltage_array)):
            dump = []
            new_time_array = self.divided_time_array[i]
            new_voltage_array = self.divided_voltage_array[i]
            max_peaks = []

            tmp_max, tmp_min = -np.Inf, np.Inf  # tmp var to hold max, min

            for index, (pos, curr_val) in enumerate(zip(new_time_array,
                                                        new_voltage_array)):
                if curr_val > tmp_max:  # if current value is > tmp
                    max_pos = pos
                    tmp_max = curr_val  # tmp = current

                if curr_val < tmp_min:
                    tmp_min = curr_val

                # Look for local max
                if curr_val < tmp_max:
                    if tmp_max != np.Inf:
                        if new_voltage_array[index:index +
                                             self.MIN_DIST].max() < tmp_max:
                            # Found a valid peak
                            dump.append(True)
                            max_peaks.append([max_pos, tmp_max])
                            # Setting flags to show that a peak was found
                            tmp_min = np.Inf
                            tmp_max = np.Inf
                            if index + self.MIN_DIST >= len(new_voltage_array):
                                # window exceeds signal length
                                break
                            continue
                # Now, look for local min - using this search
                # to eliminate smaller peaks that aren't local peaks
                # Prevents collecting the same max peak multiple times
                if curr_val > tmp_min:
                    if tmp_min != -np.Inf:
                        # Found a min point
                        if new_voltage_array[index:index +
                                             self.MIN_DIST].min() > tmp_min:
                            dump.append(False)
                            # Setting flags to show that min point was found
                            tmp_min = -np.Inf
                            tmp_max = -np.Inf  # Trigger max peak finding
                            if index + self.MIN_DIST >= len(new_voltage_array):
                                # window exceeds signal length
                                break

            self.total_peaks.append(max_peaks)
            # Remove the false hit on the first value
            try:
                if dump[0]:
                    max_peaks.pop(0)
                del dump
            except IndexError:
                    # no peaks were found
                    print("No peaks were found")

    def get_inst_hr(self):
        """
           Method that calculates inst heart rate every update_time seconds
           by counting number of peaks occurring within update_time

           :returns: none
           """

        num_of_peaks = []
        peak_pos = []
        x = []
        if isinstance(self.update_time, float):
            self.update_time = int(self.update_time)
        for i in range(len(self.total_peaks)):
            num_of_peaks.append(len(self.total_peaks[i]))
            peak_pos.append(self.total_peaks[i][-1][0])
        new_array = np.array(num_of_peaks)
        inst_heart_rate = (new_array / self.update_time)*60
        for i in range(len(peak_pos)):
            x.append(np.argmax(self.time_array == peak_pos[i]))
        for j in range(len(x)):
            last = np.argmax(self.raw_bunches == 0)
            self.raw_bunches[last:x[j]] = inst_heart_rate[j]

    def get_avghr(self):
        """

            Method gets avghr over user-specified minutes window.
            Also gives clinical indication of tachy/bradycardia,
            based on threshold values

            :returns: none

        """

        self.rounded_max = int(math.floor(max(self.time_array)))
        self.data_min = int(min(self.time_array))
        self.total_time = self.rounded_max - min(self.time_array)

    # User specified seconds is more than data set time
        if self.user_sec > self.total_time:
            # self.real_bunches = np.array_split(self.raw_bunches, len(self.raw_bunches))
            self.avg_hr = np.mean(self.raw_bunches)

    # User specified seconds is <= data set time
        else:
            # self.real_bunches = chunks(len(self.raw_bunches), self.groups)
            # for i in range(0, len(self.raw_bunches), self.user_sec):
                # self.real_bunches.append(self.raw_bunches[i:i + self.groups])
            # for i in range(len(self.real_bunches)):
                # self.avg_hr.append(np.mean(self.real_bunches[i], axis=0))
            for i in range(self.data_min, self.rounded_max, self.user_sec):
                self.indices.append(((np.abs(self.time_array-i)).argmin()))
            # When only one index is reported (avg window is large for data)
            if isinstance(self.indices, np.int64) is True:
                self.real_bunches.append(self.raw_bunches[0:self.indices])
                self.real_bunches.append(self.raw_bunches[self.indices:-1])
            else:
                for i in range(1, len(self.indices)):
                    self.real_bunches.append(self.raw_bunches[self.indices[i-1]:self.indices[i]])
            for i in range(len(self.real_bunches)):
                self.avg_hr.append(np.mean(self.real_bunches[i], axis=0))

    # Calculating brady-/tachycardia
        for i in range(len(self.raw_bunches)):
            if np.logical_and(self.raw_bunches[i] > self.brady_threshold,
                              self.raw_bunches[i] < self.tachy_threshold):
                self.tachy.append('False')
                self.brady.append('False')
            if self.raw_bunches[i] >= self.tachy_threshold:
                self.tachy.append('True')
                self.brady.append('False')
            elif self.raw_bunches[i] <= self.brady_threshold:
                self.tachy.append('False')
                self.brady.append('True')

    def summary(self):
        """
        Return the values(time, inst_HR, tachycardia, bradycardia)
        are in json format.
        :return: None
        """
        self.ecg_summary = {
            "time":self.time_array,
            "instantaneous_heart_rate": self.raw_bunches,
            "tachycardia_annotations": self.tachy,
            "bradycardia_annotations": self.brady
        }

    def as_dict(self):
        """
        Returns previous attributes as dictionaries for easier jsonification.
        :returns: none
        """
        self.ecg_dict = {
            "averaging_period": self.user_sec,
            "time_interval": self.time_array,
            "average_heart_rate": self.avg_hr,
            "tachycardia_annotations": self.tachy,
            "bradycardia_annotations": self.brady,
        }

    def get_output(self):
        """
        Method to save HR output information to a .txt file
        
        :returns: none
        """

        hr_info = open('{}_HR_Information.txt'.format(self.name), 'w')
        hr_info.write("Estimated Instantaneous HR is {} beats per minute.\n"
                      .format(self.raw_bunches))
        hr_info.write("\nEstimated Average HR is {} beats per minute with an averaging"
                      " window of {} seconds.\n"
                      .format(self.avg_hr, self.user_sec))
        hr_info.write("\n Tachycardia array is {}.\n".format(self.tachy))
        hr_info.write("\n Bradycardia array is {}.\n".format(self.brady))
