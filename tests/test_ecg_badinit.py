import unittest
import numpy as np
from get_ecg import Ecg


class TestEcgBadInit(unittest.TestCase):

    def test_string_error(self):
        self.assertRaises(ValueError, Ecg(csv_file='ecg_data_short.csv',
                                          update_time='n'))
        self.assertRaises(ValueError, Ecg(csv_file='ecg_data_short.csv',
                                          update_time=2, mins='n'))
        self.assertRaises(ValueError, Ecg(csv_file='ecg_data_short.csv',
                                          update_time=2,
                                          brady_threshold='x', mins=2))
        self.assertRaises(ValueError, Ecg(csv_file='ecg_data_short.csv',
                                          update_time=2,
                                          brady_threshold='x',
                                          tachy_threshold='b'))