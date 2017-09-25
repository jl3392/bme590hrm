# Importing dependencies

# Importing necessary fxns
# from hrm1 import find_max_peaks
# from hrm1 import inst_hr
# from hrm1 import avg_hr
from avg_hr import new_hr_set
from avg_hr import avg_hr
import unittest


def test_new_hr_set_equal():
    """
    Checks for when user input exists in set for half a minute (300 sec)
    """
    mins = 0.5
    rawbunches = [80, 79, 85, 90, 77, 73]
    testgroup = new_hr_set(mins, rawbunches)
    assert testgroup[1] == 6


def test_new_hr_set_between():
    """
    Checks for when user input is not divisible by predetermined window (e.g. 0.67 min)
    """
    min2 = 0.67
    rawbunches = [80, 79, 85, 90, 77, 73]
    testgroup2 = new_hr_set(min2, rawbunches)
    assert testgroup2[1] == 9


def test_longmin():
    """
    Checking a larger user input, as well as a user input of type 'int'
    """
    minlong = 132
    rawbunches = [80, 79, 85, 90, 77, 73]
    testgrouplong = new_hr_set(minlong, rawbunches)
    assert testgrouplong[1] == 1584


class TestComplex(unittest.TestCase):
    def test_complex(self):
        """
        Testing for 'raise' error when input is set to a complex number
        """
        rawbunches = [80, 79, 85, 90, 77, 73]
        self.assertRaises(ValueError, new_hr_set, 2j+9, rawbunches)


def test_groupnum_greaterthan_data():
    """
    This tests when user inputs a time greater than the data set allows
    """
    mins = 5  # User input 5 minutes
    rawbunches = [65, 70, 68, 77, 74, 68, 64, 65, 64, 78]  # Data set only has bunches for 50 sec
    testinputgreater = new_hr_set(mins, rawbunches)
    assert testinputgreater[0] == rawbunches


def test_groupnum_equaltodata():
    """
    Tests when user inputs a time equal to data set
    """
    mins = 0.5
    rawbunches = [60, 70, 65, 68, 71, 68]
    testinputequal = new_hr_set(mins, rawbunches)
    assert testinputequal[0] == rawbunches


def test_groupnum_lessthandata():
    """
    Tests when input is less than data set
    """
    mins = 0.5  # 30 sec input
    rawbunches = [60, 70, 65, 68, 71, 68, 66, 65, 73, 69, 66, 62]  # Minute worth of data
    testinputless = new_hr_set(mins, rawbunches)
    assert testinputless[0] == [60, 70, 65, 68, 71, 68]  # Output should be half a min


def test_avg_hr():
    """
    Simple averaging
    """
    realbunches = [80, 79, 85, 90, 77, 73]
    groupnum = 6
    assert avg_hr(realbunches, groupnum) == 80


def test_avg_hr_float():
    """
    Testing with float values
    """
    realbunches = [80.1, 87.5, 83.4, 90, 76.5]
    groupnum = 5
    assert avg_hr(realbunches, groupnum) == 83








