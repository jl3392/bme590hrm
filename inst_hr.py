import numpy as np
import opencsv


def inst_hr(detected_peaks, update_time):
    """
    Function that calculates instantaneous heart rate every update_time seconds
    by counting number of peaks within update_time

    :param detected_peaks: list of detected peaks
    :param update_time: How often the instantaneous HR must be updated in s
    :type detected_peaks: list
    :type update_time: int/float
    :return inst_heart_rate: calculated instantaneous heart rate
    :rtype: nd array

    """
    num_of_peaks = []
    if isinstance(update_time, float):
        update_time = int(update_time)
    for i in range(len(detected_peaks)):
        num_of_peaks.append(len(detected_peaks[i]))
    new_array = np.array(num_of_peaks)
    inst_heart_rate = new_array / update_time
    return inst_heart_rate * 60
