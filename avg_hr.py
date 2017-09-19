# Need to import Niranjana's Module for Inst. HR
from inst_hr import inst_hr

# Initialization
min2sec = 60
inst_time_period = 5  # In minutes

def new_hr_set(mins):
    # Taking input and converting it to seconds
    mins = float(input('Please specify a time (in min) for averaging.'))

    # if isinstance(mins,complex) = True:
    #   print('Please use real numbers.')

    # Conversion of minutes to seconds
    usersec = mins * min2sec

    # Must have number of groups be whole
    if usersec % inst_time_period is True:
        groupnum = usersec/inst_time_period
    # Taking an additional groups if user input is between groups
    elif usersec % inst_time_period is False:
        groupnum = round(usersec/inst_time_period) + 1

    # Take Niranjana's grouping output and truncating to fit user input
    rawbunches = inst_hr()
    realbunches = rawbunches[:groupnum]
    return realbunches, groupnum


def avg_hr(realbunches, groupnum):
    avghr = sum(realbunches)/groupnum
    return avghr()
    print('The average heart rate for {} minute(s) was {} beats per minute'.format(mins, avghr))







