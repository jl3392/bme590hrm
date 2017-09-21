# Importing dependencies

# Importing necessary fxns
# from hrm1 import find_max_peaks
# from hrm1 import inst_hr
# from hrm1 import avg_hr




def test_new_hr_set_equal():
    # This case checks for when user input exists in set for 5 minutes (300 sec)
    testgroup = new_hr_set('5')
    assert testgroup[1] == 60


def test_new_hr_set_between():
    # This case checks for when user input is not divisible by predetermined window
    testgroup2 = new_hr_set('5.1')
    assert testgroup22[2] == 61

# TO DO - Raise exception for when user input is a NaN or a complex number


def test_avg_hr():
    assert avg_hr([80, 79, 85, 90, 77], 5) == 82.2









