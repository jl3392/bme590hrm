# Need to import Niranjana's Module for Inst. HR
# from inst_hr import inst_hr
import math


# Initialization
min2sec = 60
inst_time_period = 5  # In seconds


def new_hr_set(mins):
    # Taking input and converting it to seconds
    if isinstance(mins, float) is True:
        mins = mins
    else:
        mins = input('Please specify a time (in min) for averaging.')

    if isinstance(mins, complex) is True:
        print('Please use real numbers.')

    # Conversion of minutes to seconds
    usersec = mins * min2sec

    # Must have number of groups be whole
    if usersec % inst_time_period == 0:
        groupnum = int(usersec/inst_time_period)
    # Taking an additional groups if user input is between groups
    else:
        groupnum = int(math.floor(usersec/inst_time_period) + 1)

    # Take Niranjana's grouping output and truncating to fit user input
    rawbunches = [80, 79, 85, 90, 77, 73]  # test data, should be inst_hr()
    realbunches = rawbunches[0:groupnum]
    return realbunches, groupnum


def avg_hr(realbunches, groupnum):
    avghr = math.floor(sum(realbunches)/groupnum)
    return avghr
    # print('The average heart rate for {} minute(s) was {} beats per minute'.format(mins, avghr))







