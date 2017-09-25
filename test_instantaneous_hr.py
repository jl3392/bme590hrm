from find_max_peaks import find_max_peaks
import numpy as np
from opencsv import opencsv

f = opencsv('Data\ecg_data_short.csv')
sample_time_array = f[0]
sample_voltage_array = f[1]


def test_find_max_peaks():
    """
    Unit test for function that finds and counts R peaks of all QRS modules within specified inst_time_period_secs
    """
    peaks = find_max_peaks(voltage_array=sample_voltage_array, time_array=sample_time_array, min_dist=150,
                             update_time=3)
    assert peaks == [[[8.6739999999999995, 0.54249999999999998], [9.3260000000000005, 0.59950000000000003]], [[9.9879999999999995, 0.63800000000000001], [10.654, 0.64949999999999997]], [[11.318, 0.66849999999999998], [11.952, 0.64749999999999996]]]
    return peaks

def test_inst_hr():
    """
    Unit test for function that calculates instantaneous HR
    :return: nothing, pass if assertion is true
    
    """
    from inst_hr import inst_hr
    peaks = test_find_max_peaks()

    HR = inst_hr(peaks,update_time =3)  #in bpm
    checking_HR = np.array(HR == [40,40,40])

    assert checking_HR.all()



