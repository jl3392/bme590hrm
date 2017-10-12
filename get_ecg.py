class get_ecg:

    def get_avghr(self):
        """ returns avghr

            Function gets avghr over user-specified minutes window.
            Also gives clinical indication of tachy/bradycardia
        """

        if isinstance(mins, float) is True or isinstance(mins, int) is True:
            mins = mins
        elif isinstance(mins, complex) is True:
            raise ValueError('Please use real numbers.')

        user_sec = mins * self.min2sec

    # Must have number of groups be whole
        if user_sec % self.update_time == 0:
            group_num = int(user_sec/self.update_time)
        # Taking an additional groups if user input is between groups
        else:
            group_num = int(math.floor(user_sec/self.update_time) + 1)

        # Take Niranjana's grouping output and truncating to fit user input
        if len(self.raw_bunches) <= group_num:  # if user time is > raw data
            real_bunches = self.raw_bunches
        else:
            real_bunches = self.raw_bunches[0:group_num]
            
    # Calculating the avghr
        avg_hr = math.floor(sum(real_bunches)/len(real_bunches))
        return avg_hr

    # Calculating brady-/tachycardia
        if self.brady_threshold < avg_hr < self.tachy_threshold:
            status = [2, 'You have a normal average heart rate '
                         'over the period of {} minutes'.format(mins)]
        elif avg_hr >= self.tachy_threshold:
            status = [1, 'You have tachycardia over the '
                         'period of {} minutes'.format(mins)]  # Tachy
        elif avg_hr <= self.brady_threshold:
            status = [0, 'You have bradycardia over '
                         'the period of {} minutes'.format(mins)]  # Brady

        return status
