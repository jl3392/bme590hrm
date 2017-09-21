import numpy as np


def find_max_peaks(voltage_array, time_array, min_dist):
    """
    Function that will find local maxima of an array i.e maximum peaks

    :voltage_array - The array containing the signal from which peaks are to be detected
    :time_array - An array corresponding to the voltage array that has the same length
    :min_dist - How many data points to wait before detecting a peak
    """

    max_peaks = []
    dump = []  # Used to pop the first hit which almost always is false
    length = len(voltage_array)

    if min_dist < 1:
        raise ValueError("Lookahead must be '1' or above in value")

    mx, mn = -np.Inf, np.Inf

    for index, (x, y) in enumerate(zip(time_array[:-min_dist],
                                       voltage_array[:-min_dist])):
        if y > mx:
            mx = y
            mx_pos = x
        if y < mn:
            mn = y

        if y < mx and mx != np.Inf:
            # Found a peak
            if voltage_array[index:index + min_dist].max() < mx:
                max_peaks.append([mx_pos, mx])
                dump.append(True)
                # set algorithm to only find minima now
                mn = np.Inf
                mx = np.Inf
                if index + min_dist >= length:
                    # end is within min_dist no more peaks can be found
                    break
                continue

        if y > mn and mn != -np.Inf:
            # using this dependency to keep finding maximas - don't know how to get around not using this part
            if voltage_array[index:index + min_dist].min() > mn:
                dump.append(False)
                # set algorithm to only find maxima now
                mn = -np.Inf
                mx = -np.Inf
                if index + min_dist >= length:
                    # end is within min_dist no more peaks can be found
                    break

    # Remove the false hit on the first value of the y_axis
    try:
        if dump[0]:
            max_peaks.pop(0)
        del dump
    except IndexError:
        # no peaks were found, should the function return empty lists?
        print("No peaks were found")

    return [max_peaks]