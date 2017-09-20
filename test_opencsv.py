import opencsv
import numpy


filename = "Data/ecg_data_short.csv"


def test_opencsv():

    f = opencsv.opencsv(filename)
    if isinstance(f, numpy.ndarray) is True:
        print("The csv file is open and imported as dictionary")


def check_empty():
    f = opencsv.opencsv(filename)
    assert len(f) != 0

