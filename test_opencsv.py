import opencsv
import numpy


filename = "Data/ecg_data_short.csv"


def test_opencsv():
    """test the return values( time and voltage) are in numpy array format
    """

    f = opencsv.opencsv(filename)
    if isinstance(f, numpy.ndarray) is True:
        print("The csv file is open and imported as dictionary")


def check_empty():
    """test the file is not empty
    """

    f = opencsv.opencsv(filename)
    assert len(f) != 0

