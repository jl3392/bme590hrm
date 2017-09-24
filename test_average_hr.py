# Importing dependencies

# Importing necessary fxns
# from hrm1 import find_max_peaks
# from hrm1 import inst_hr
# from hrm1 import avg_hr
from avg_hr import new_hr_set
from avg_hr import avg_hr


def test_new_hr_set_equal():
    # This case checks for when user input exists in set for half a minute (300 sec)
    mins = 0.5
    testgroup = new_hr_set(mins)
    assert testgroup[1] == 6


def test_new_hr_set_between():
    # This case checks for when user input is not divisible by predetermined window
    min2 = 0.6
    testgroup2 = new_hr_set(min2)
    assert testgroup2[1] == 8

# TO DO - Raise exception for when user input is a NaN or a complex number


def test_avg_hr():
    realbunches = [80, 79, 85, 90, 77, 73]
    groupnum = 6
    assert avg_hr(realbunches, groupnum) == 80








