# Importing Dependencies

# Importing necessary fxns
from bradtach import bradtach

def test_normal():
    assert bradtach(80, 100, 60) == 2

def test_brady():
    assert bradtach(30, 100, 60) == 0

def test_tachy():
    assert bradtach(120, 100, 60) == 1



