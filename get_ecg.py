class GetEcg:
    """
    Creating this class to convert raw ECG data of all types into HR data
    and clinical indication of brady-/tachycardia.
    """
    min2sec = 60

    def __init__(self,csv_file=None, update_time=5, brady_threshold = 60, tachy_threshold = 100):
        """
        Constructor for ECG processing needs the input csv file to work on and
        time for often to update the instantaneous HR

        :param csv_file: the input file containing ECG data
        :param update_time: instantaneous HR update time
        :param brady_threshold: threshold for bradycardia
        :param tachy_threshold: threshold for tachycardia
        """
        if csv_file is not None:
            data = np.loadtxt(csv_file, dtype='float', delimiter=",",
                              skiprows=0)
            self.time_array = np.array(data[:, 0])
            self.voltage_array = np.array(data[:, 1])
            self.update_time = update_time
            self.brady_threshold = brady_threshold
            self.tachy_threshold = tachy_threshold

        self.raw_bunches = []



