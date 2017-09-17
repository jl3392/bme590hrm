from hmr1 import opencsv


def test_opencsv():
    f = opencsv("file_name.csv")
    if isinstance(f, dict) is True:
        print("The csv file is open and imported as dictionary")


def check_header():
    f = opencsv("file_name.csv")
    assert f.head(1) == ['time(s)', 'voltage(mv)']


def check_empty():
    f = opencsv("file_name.csv")
    assert len(f) != 0

