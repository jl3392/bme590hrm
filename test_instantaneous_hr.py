import find_max_peaks
import inst_hr
import numpy as np

sample_voltage_array1 = np.array([0.411, 0.388, 0.3345, 0.386, 0.3475]) #in mv
sample_time_array1 = np.array([0,1,2,3,4])#in seconds

sample_voltage_array2 = np.array([0.411,0.388, 0.3345, 0.386, 0.3475, 0.3470, 0.3600,0.3575,0.3770, 0.3575])
sample_time_array2 = np.array([0,1,2,3,4,5,6,7,8,9])

sample_voltage_array3 = np.array([0.411, 0.388, 0.3345, 0.386, 0.3475,0.3470,0.3440])
sample_time_array3 = np.array([0,1,2,3,4,5,6])


def test_find_max_peaks():
    """
    Unit test for function that finds and counts R peaks of all QRS modules within specified inst_time_period_secs
    """
    index_of_peaks1 = find_max_peaks(sample_voltage_array1,inst_time_period = 5)
    index_of_peaks2 = find_max_peaks(sample_voltage_array2, inst_time_period = 5)
    index_of_peaks3 = find_max_peaks(sample_voltage_array3, inst_time_period = 5)

    assert index_of_peaks1 == [1,3]
    assert index_of_peaks2 == [[1,3],[6,8]]
    assert index_of_peaks3 == [1,3]
    
    return (len(index_of_peaks1),len(index_of_peaks2),len(index_of_peaks3))

def test_inst_hr():
    """
    Unit test for function that calculates instantaneous HR
    :return: nothing, pass if assertion is true
    """
    (num_of_peaks1,num_of_peaks2,num_of_peaks3) = test_find_max_peaks()

    assert inst_hr(num_of_peaks1) == 24 #in bpm
    assert inst_hr(num_of_peaks2) == [24,24] 
    assert inst_hr(num_of_peaks3) == 24



