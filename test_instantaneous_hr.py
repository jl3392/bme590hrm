import find_max_peaks
import inst_hr
import numpy as np

sample_voltage_array = np.array([0.411, 0.388, 0.3345, 0.386, 0.3475, 0.35, 0.3575, 0.3645, 0.3515, 0.324, 0.2965])
sample_time_array = np.array([8,8.002,8.004,8.006,8.008,8.01,8.012,8.014,8.016,8.018,8.02])

# TODO: Use bigger data sets
#TODO: Update : This is a teriible unit test. To be rescripted today 9/19


def test_find_max_peaks():
    """
    Unit test for function that finds R peaks of all QRS modules in the ECG trace
    """
    index_of_peaks = find_max_peaks(sample_voltage_array)

    assert index_of_peaks == [3, 7]
    assert len(index_of_peaks) == 2
    return len(index_of_peaks)


def test_inst_hr():
    """
    Unit test for function that calculates instantaneous HR
    :return: pass if assertion is true
    """
    index_of_peaks = test_find_max_peaks()
    indexed_time = sample_time_array[index_of_peaks]

    assert inst_hr(indexed_time) == 30000 # unrealistic but just checking the math



