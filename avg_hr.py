# Need to import Niranjana's Module for Inst. HR

# Headers
min2sec = 60
# Ask Niranjana what she called this variable
blockwindow = 5


def new_hr_set(mins):
    # Taking input and converting it to seconds
    mins = float(input('Please specify a time (in min) for averaging.'))

    # if isinstance(mins,complex) = True:
    #   print('Please use real numbers.')

    # Conversion of minutes to seconds
    usersec = mins * min2sec

    # Must have number of groups be whole
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
    return avghr()
    print('The average heart rate for {} minute(s) was {} beats per minute'.format(mins, avghr))







