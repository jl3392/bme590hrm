# Importing dependencies

# Importing necessary fxns
from hrm1 import find_max_peaks
from hrm1 import inst_hr
from hrm1 import avg_hr

from avg_hr import new_hr_set
from avg_hr import avg_hr

def test_new_hr_set_exists():
    # This case checks for when user input exists in set for 5 minutes (300 sec)
    assert new_hr_set(300, [80,200,250,270,300,301,400]) == [80,200,250,270,300]

def test_new_hr_set_DNEinside():
    # This case checks for when user input does not exist, and is within the limits
    assert new_hr_set(300, [80,200,250,280,320,800,9000]) == [80,200,250,280,320]

def test_new_hr_set_DNEoutside():
    # This case checks for when user input does not exist, and is outside of the limit
    assert new_hr_set(300, [80,200,250,280]) == [80,200,250,280]

# TO DO - Raise exception for when user input is a NaN or a complex number

def test_avg_hr():
    assert avg_hr(5, [80,200,250,280,320]) == #Will calculate this once inst_hr exists







