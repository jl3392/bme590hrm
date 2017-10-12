import numpy as np


def find_max_peaks(voltage_array, time_array, update_time, min_dist=150):
    """
    Function that will find local maximum of an array i.e peaks

       :param voltage_array: signal from which peaks are to be detected
       :param time_array: An array of same length as the voltage array
       :param min_dist: How many data points to wait before looking for peaks
       :param update_time: How often the instantaneous HR must be updated in s
       :type voltage_array: nd array
       :type time_array: nd array
       :type min_dist: int
       :type update_time: int/float
       :return total_peaks: list of all peaks detected within update_time
       :rtype: list

    """
    total_peaks = []

    if isinstance(update_time, float):
        update_time = int(update_time)
    total_time = time_array[-1] - time_array[1]
    bunches = total_time/update_time
    if total_time / update_time < 1:
        raise ValueError("Update time is longer than signal length")
    divided_voltage_array = np.array_split(voltage_array, bunches)
    divided_time_array = np.array_split(time_array, bunches)
    length = len(voltage_array)
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
