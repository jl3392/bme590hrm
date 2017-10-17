import unittest
import numpy as np
from get_ecg import Ecg


class TestEcgBadInit(unittest.TestCase):

    def test_string_error(self):
        val = 'x'
        file = 'ecg_data_short.csv'
        self.assertRaises(ValueError, Ecg, file, val)
        self.assertRaises(ValueError, Ecg, csv_file=file,
                          update_time=2, mins=val)
        self.assertRaises(ValueError, Ecg, csv_file=file,
                          update_time=2, brady_threshold=val, mins=2)
        self.assertRaises(ValueError, Ecg, csv_file=file,
                          update_time=2, brady_threshold=val,
                          tachy_threshold=val)
