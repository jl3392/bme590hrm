class get_ecg:
    """
    Creating this class to convert raw ECG data of all types into HR data and clinical indication of brady-/tachycardia.
    """

    def __init__(self, opencsv):
        self.opencsv = opencsv

    def get_max_peak(self):
        total_peaks =[]
        if isinstance(self.update_time, float):
         update_time = int(self.update_time)
         total_time = self.time_array[-1] - self.time_array[1]
         bunches = total_time/update_time

        if total_time / update_time < 1:
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

    def get_inst_hr(self,get_max_peak):

        num_of_peaks = []
        if isinstance(self.update_time, float):
            update_time = int(self.update_time)
        for i in range(len(get_max_peak)):
            num_of_peaks.append(len(get_max_peak[i]))
        new_array = np.array(num_of_peaks)
        inst_heart_rate = new_array / self.update_time
        return inst_heart_rate * 60


