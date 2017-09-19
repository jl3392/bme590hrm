# Need to import Niranjana's Module for Inst. HR
<<<<<<< HEAD
from inst_hr import inst_hr

# Initialization
min2sec = 60
inst_time_period = 5  # In minutes
=======

# Headers
min2sec = 60
# Ask Niranjana what she called this variable
blockwindow = 5

>>>>>>> 7d7b8cccf8e981168cef7d796688fa1231140d93

def new_hr_set(mins):
    # Taking input and converting it to seconds
    mins = float(input('Please specify a time (in min) for averaging.'))

    # if isinstance(mins,complex) = True:
    #   print('Please use real numbers.')

    # Conversion of minutes to seconds
    usersec = mins * min2sec

    # Must have number of groups be whole
<<<<<<< HEAD
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
=======
    if usersec % blockwindow is True:
        groupnum = usersec/blockwindow
    # Taking an additional groups if user input is between groups
    elif usersec % blockwindow is False:
        groupnum = round(usersec/blockwindow) + 1

    # Take Niranjana's grouping output and truncating to fit user input
    bunches = niranj()
    return bunches, groupnum


def avg_hr(bunches,groupnum):
    avghr = sum(bunches)/groupnum
>>>>>>> 7d7b8cccf8e981168cef7d796688fa1231140d93
    return avghr()
    print('The average heart rate for {} minute(s) was {} beats per minute'.format(mins, avghr))







