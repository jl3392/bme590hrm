class get_ecg:
    """
    Creating this class to convert raw ECG data of all types into HR data and clinical indication of brady-/tachycardia.
    """

    def __init__(self,opencsv):
        self.opencsv = opencsv

    def get_avghr(self):
        if isinstance(mins, float) is True or isinstance(mins, int) is True:
            mins = mins
        elif isinstance(mins, complex) is True:
            raise ValueError('Please use real numbers.')

        usersec = mins * self.min2sec

    # Must have number of groups be whole
        if usersec % self.update_time == 0:
            groupnum = int(usersec/self.update_time)
        # Taking an additional groups if user input is between groups
        else:
            groupnum = int(math.floor(usersec/self.update_time) + 1)

        # Take Niranjana's grouping output and truncating to fit user input
        # rawbunches = [80, 79, 85, 90, 77, 73]  # test data, should be inst_hr()
        if len(self.rawbunches) <= groupnum:  # Case for if user specified time is > number of indices of actual data
            realbunches = self.rawbunches
        else:
            realbunches = self.rawbunches[0:groupnum]

    # Calculating the avghr
        avghr = math.floor(sum(realbunches) / groupnum)
        return avghr

    # Calculating brady-/tachycardia
        if bradythreshold < avghr < tachythreshold:
            status = [2, 'You have a normal average heart rate over the period of {} minutes'.format(mins)]  # Normal
        elif avghr >= tachythreshold:
            status = [1, 'You have tachycardia over the period of {} minutes'.format(mins)]  # Tachycardia
        elif avghr <= bradythreshold:
            status = [0, 'You have bradycardia over the period of {} minutes'.format(mins)]  # Bradycardia

        return status
