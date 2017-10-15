import numpy as np
import math


class GetEcg:

    """
    Creating this class to convert raw ECG data of all types into HR data
    and clinical indication of brady-/tachycardia.
    """
    min2sec = 60

    def __init__(self, csv_file=None, update_time=5,
                 brady_threshold=60, tachy_threshold=100):
        """
        Constructor for ECG processing needs the input csv file to work on and
        time for often to update the instantaneous HR

        :param csv_file: the input file containing ECG data
        :param update_time: instantaneous HR update time in seconds
        :param brady_threshold: threshold for bradycardia in bpm
        :param tachy_threshold: threshold for tachycardia in bpm
        """
        if csv_file:
            data = np.loadtxt(csv_file, dtype='float', delimiter=",",
                              skiprows=0)
            self.time_array = np.array(data[:, 0])
            self.voltage_array = np.array(data[:, 1])
            self.update_time = update_time
            self.brady_threshold = brady_threshold
            self.tachy_threshold = tachy_threshold

        self.raw_bunches = raw_bunches
        self.total_peaks = total_peaks
        self.divided_voltage_array = np.array([])
        self.divided_time_array = np.array([])

    def prep_data(self):
        """
        Method that prepares data for get_max_peaks
        :return: none
        """
        total_time = self.time_array[-1] - self.time_array[1]
        groups = total_time / self.update_time  # inst HR groups

        if groups < 1:
            raise ValueError("Update time is longer than signal length")
        self.divided_voltage_array = np.array_split(self.voltage_array, groups)
        self.divided_time_array = np.array_split(self.time_array, groups)
        length = len(self.voltage_array)

        if length % bunches != 0:  # ignore last group if not equal to others
            np.delete(self.divided_voltage_array, -1)

    def get_max_peak(self):
        """
           Method that will find local maximum of an array i.e peaks

              :return total_peaks: list of all peaks detected, arranged
               into chunks based on update_time
              :rtype: list

           """
        total_peaks = []
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
                        if new_voltage_array[index:index + min_dist].max() < mx:
                            # Found a valid peak
                            dump.append(True)
                            max_peaks.append([max_pos, mx])
                            # Setting flags to show that a peak was found
                            mn = np.Inf
                            mx = np.Inf
                            if index + min_dist >= length:
                                # signal ends before end of window, no more valid peaks can be found
                                break
                            continue
                # Now, look for local min - using this search to eliminate smaller peaks that
                # are not local peaks
                # Prevents collecting the same max peak multiple times
                if y > mn:
                    if mn != -np.Inf:
                        # Found a min point
                        if new_voltage_array[index:index + min_dist].min() > mn:
                            dump.append(False)
                            # Setting flags to show that min point was found
                            mn = -np.Inf
                            mx = -np.Inf # Triggering max peak finding again
                            if index + min_dist >= length:
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
            return total_peaks

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
        return self.raw_bunches

    def get_avghr(self):
        """ returns avghr

            Function gets avghr over user-specified minutes window.
            Also gives clinical indication of tachy/bradycardia

            :return avg_hr: Avg hr
            :return status: Brady or tachycardia
        """
        mins = float(input('Please specify a time (in min) for averaging.'))
        if isinstance(mins, float) is True or isinstance(mins, int) is True:
            mins = mins
        elif isinstance(mins, complex) is True:
            raise ValueError('Please use real numbers.')

        user_sec = mins * self.min2sec

    # Must have number of groups be whole
        if user_sec % self.update_time == 0:
            group_num = int(user_sec/self.update_time)
        # Taking an additional groups if user input is between groups
        else:
            group_num = int(math.floor(user_sec/self.update_time) + 1)

        # Take Niranjana's grouping output and truncating to fit user input
        if len(self.raw_bunches) <= group_num:  # if user time is > raw data
            real_bunches = self.raw_bunches
        else:
            real_bunches = self.raw_bunches[0:group_num]

    # Calculating the avghr
        avg_hr = math.floor(sum(real_bunches)/len(real_bunches))

    # Calculating brady-/tachycardia
        if self.brady_threshold < avg_hr < self.tachy_threshold:
            status = [2, 'You have a normal average heart rate '
                         'over the period of {} minutes'.format(mins)]
        elif avg_hr >= self.tachy_threshold:
            status = [1, 'You have tachycardia over the '
                         'period of {} minutes'.format(mins)]  # Tachy
        elif avg_hr <= self.brady_threshold:
            status = [0, 'You have bradycardia over '
                         'the period of {} minutes'.format(mins)]  # Brady

        return [status, avg_hr]
