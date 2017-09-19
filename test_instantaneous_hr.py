import find_max_peaks
import inst_hr
import numpy as np

sample_voltage_array = np.array([0.411, 0.388, 0.3345, 0.386, 0.3475]) #in mv
sample_time_array = np.array([0,1,2,3,4])#in seconds

#TODO: Use bigger data sets to get multiple cardiac beats
#TODO: Use data sets with of length that is not fully divisible by 5. Want : func ignores leftover values

def test_find_max_peaks():
    """
    Unit test for function that finds and counts R peaks of all QRS modules within specified inst_time_period_secs
    """
    index_of_peaks = find_max_peaks(sample_voltage_array,inst_time_period_secs = 5)

    assert index_of_peaks == [1,3]
    return len(index_of_peaks)


def test_inst_hr():
    """
    Unit test for function that calculates instantaneous HR
    :return: nothing, pass if assertion is true
    """
    num_of_peaks = test_find_max_peaks()
    assert inst_hr(num_of_peaks) == 24 #in bpm  



