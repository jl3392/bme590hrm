import unittest
import numpy as np
from get_ecg import Ecg


class TestEcgBadData(unittest.TestCase):
    data = Ecg(csv_file='ecg_data_bad.csv', update_time=2)
    data.prep_data()
    data.get_max_peak()
    data.get_inst_hr()
    data.get_avghr()

    def test_data_array(self):
        self.assertIsInstance(self.data.voltage_array,
                              (np.ndarray, np.generic))
        self.assertIsInstance(self.data.time_array,
                              (np.ndarray, np.generic))

        # Check if bad string in input was removed
        self.assertEqual(self.data.voltage_array[8],
                         self.data.voltage_array[7])
        self.assertEqual(self.data.time_array[13], self.data.time_array[12])

    def test_prep_data(self):
        self.assertEqual(len(self.data.divided_voltage_array), 1)
        self.assertEqual(len(self.data.divided_time_array), 1)

    def test_get_max_peak(self):
        sample_peaks = [[[8.6739999999999995, 0.54249999999999998],
                         [9.3260000000000005, 0.59950000000000003],
                         [9.9879999999999995, 0.63800000000000001],
                         [10.654000000000002, 0.64949999999999997],
                         [11.318, 0.66849999999999998]]]
        self.assertEqual(self.data.total_peaks, sample_peaks)

    def test_inst_hr(self):
        sample_raw_bunches = [1.500000000000000000e+02]
        self.assertEqual(self.data.raw_bunches, sample_raw_bunches)

    def test_avg_hr(self):
        sample_avg_hr = 150
        self.assertEqual(self.data.avg_hr, sample_avg_hr)

    # def test_status(self):
        # sample_stat = 1
        # self.assertEqual(self.data.status[0], sample_stat)
        # self.assertIsInstance(self.data.status[1], str)
