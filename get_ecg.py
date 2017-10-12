class GetEcg:

    """
    Creating this class to convert raw ECG data of all types into HR data
    and clinical indication of brady-/tachycardia.
    """
    min2sec = 60

    def __init__(self,csv_file=None, update_time=5, brady_threshold = 60, tachy_threshold = 100):
        """
        Constructor for ECG processing needs the input csv file to work on and
        time for often to update the instantaneous HR

        :param csv_file: the input file containing ECG data
        :param update_time: instantaneous HR update time
        :param brady_threshold: threshold for bradycardia
        :param tachy_threshold: threshold for tachycardia
        """
        if csv_file is not None:
            data = np.loadtxt(csv_file, dtype='float', delimiter=",",
                              skiprows=0)
            self.time_array = np.array(data[:, 0])
            self.voltage_array = np.array(data[:, 1])
            self.update_time = update_time
            self.brady_threshold = brady_threshold
            self.tachy_threshold = tachy_threshold

        self.raw_bunches = []
    def get_max_peak(self):
        """
           Function that will find local maximum of an array i.e peaks

              :type min_dist: int
              :type update_time: int/float
              :return total_peaks: list of all peaks detected, arranged into chunks based on update_time
              :rtype: list

           """
        min_dist = 150
        if isinstance(self.update_time, float):
         self.update_time = int(self.update_time)
         total_time = self.time_array[-1] - self.time_array[1]
         bunches = total_time/self.update_time

        if total_time / self.update_time < 1:
            raise ValueError("Update time is longer than signal length")
        divided_voltage_array = np.array_split(self.voltage_array, bunches)
        divided_time_array = np.array_split(self.time_array, bunches)
        length = len(self.voltage_array)

        if length % bunches != 0:
            np.delete(divided_voltage_array, -1)
         for i in range(len(divided_voltage_array)):
             dump = []
             new_time_array = divided_time_array[i]
             new_voltage_array = divided_voltage_array[i]
             max_peaks = []

             mx, mn = -np.Inf, np.Inf

             for index, (x, y) in enumerate(zip(new_time_array,
                                                new_voltage_array)):
                 if y > mx:
                     mx = y
                     mxpos = x
                 if y < mn:
                     mn = y

                 # Looking for max
                 if y < mx and mx != np.Inf:
                     # Maxima peak candidate found
                     if new_voltage_array[index:index + min_dist].max() < mx:
                         max_peaks.append([mxpos, mx])
                         dump.append(True)
                         # set algorithm to only find minima now
                         mn = np.Inf
                         mx = np.Inf
                         if index + min_dist >= length:
                             # end is within lookahead no more peaks can be found
                             break
                         continue

                 if y > mn and mn != -np.Inf:
                     if new_voltage_array[index:index + min_dist].min() > mn:
                         dump.append(False)
                         mn = -np.Inf
                         mx = -np.Inf
                         if index + min_dist >= length:
                             break

             self.total_peaks.append(max_peaks)
             # Remove the false hit on the first value of the y_axis
             try:
                 if dump[0]:
                     max_peaks.pop(0)
                 del dump
             except IndexError:
                    # no peaks were found
                    print("No peaks were found")

        return self.total_peaks


    def get_inst_hr(self, total_peaks):
        """
           Function that calculates instantaneous heart rate every update_time seconds
           by counting number of peaks within update_time
           :param total_peaks: list of detected peaks, returned using get_max_peaks function
           :type total_peaks: list
           :return self.raw_bunches: calculated instantaneous heart rate


           """
        self.total_peaks = total_peaks

        num_of_peaks = []
        if isinstance(self.update_time, float):
            self.update_time = int(self.update_time)
        for i in range(len(self.total_peaks)):
            num_of_peaks.append(len(self.total_peaks[i]))
        new_array = np.array(num_of_peaks)
        inst_heart_rate = new_array / self.update_time
        self.raw_bunches = inst_heart_rate * 60
        return self.raw_bunches        


