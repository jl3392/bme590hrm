class get_ecg:
    """
    Creating this class to convert raw ECG data of all types into HR data and clinical indication of brady-/tachycardia.
    """

    def __init__(self,opencsv):
        self.opencsv = opencsv
