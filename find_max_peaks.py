import matplotlib.pyplot as plt

import numpy as np


def find_max_peaks(voltage_array, time_array, min_dist, update_time):
    """
    Function that will find local maxima of an array i.e maximum peaks

    :voltage_array - The array containing the signal from which peaks are to be detected
    :time_array - An array corresponding to the voltage array that has the same length
    :min_dist - How many data points to wait before detecting a peak
    :update_time - How often the instantaneous HR must be updated
    """
    if isinstance(update_time, float):
        update_time = int(update_time)
    divided_voltage_array = np.array_split(voltage_array, update_time)
    length = len(voltage_array)
    chunks = len(divided_voltage_array)
    if length % update_time != 0:
        np.delete(divided_voltage_array, -1)
    for i in divided_voltage_array:
        max_peaks = []
        dump = []  # Used to pop the first hit which almost always is false

        if min_dist < 1:
            raise ValueError("Minimum must be '1' or above in value")

        mx, mn = -np.Inf, np.Inf

        # Only detect peak if there is 'lookahead' amount of points after it
        for index, (x, y) in enumerate(zip(time_array[:-min_dist],
                                           voltage_array[:-min_dist])):
            if y > mx:
                mx = y
                mxpos = x
            if y < mn:
                mn = y

            ####look for max####
            if y < mx and mx != np.Inf:
                # Maxima peak candidate found
                if voltage_array[index:index + min_dist].max() < mx:
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
                if voltage_array[index:index + min_dist].min() > mn:
                    dump.append(False)
                    ###                #set algorithm to only find maxima now
                    mn = -np.Inf
                    mx = -np.Inf
                    if index + min_dist >= length:
                        ###                    #end is within lookahead no more peaks can be found
                        break

        # Remove the false hit on the first value of the y_axis
        try:
            if dump[0]:
                max_peaks.pop(0)
            del dump
        except IndexError:
            # no peaks were found, should the function return empty lists?
            print("No peaks were found")

    return ([max_peaks], chunks)