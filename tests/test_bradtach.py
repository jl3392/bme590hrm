# Importing Dependencies

# Importing necessary functions
from bradtach import bradtach


def test_normal():
    avg_hr = 80  # Normal Adult resting HR
    mins = 1
    testnormal = bradtach(avg_hr, mins)
    assert testnormal[0] == 2


def test_brady():
    avg_hr = 60  # Adult bradycardia
    mins = 1
    testbrady = bradtach(avg_hr, mins)
    assert testbrady[0] == 0


def test_tachy():
    avg_hr = 120  # Adult tachycardia
    mins = 1
    testtach = bradtach(avg_hr, mins)
    assert testtach[0] == 1



