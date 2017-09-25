import numpy as np
import find_max_peaks
import opencsv

def inst_hr(detected_peaks, update_time):
    num_of_peaks = []
    for i in range(len(detected_peaks)):
        num_of_peaks.append(len(detected_peaks[i]))
    new_array = np.array(num_of_peaks)
    instHR = new_array / update_time
    return instHR * 60

