# Need to import Niranjana's Module for Inst. HR
# from inst_hr import inst_hr
import math


""" Average Heart Rate.

This module takes instantaneous HR inputs to output an average HR
over a time period specified by the user in minutes.
"""


# Initialization
min2sec = 60  # initializing conversion


def new_hr_set(mins, rawbunches, update_time):
    """ returns realbunches, groupnum

    This function takes in raw instantaneous heart rate based on an averaging
    window set by the user, as well as minutes specified by user input
    and returns groupnum and realbunches. Groupnum is the result of
    taking the user input,converting it to seconds, and then dividing that
    number by the amount of the instantaneous HR window duration.
    This is effectively saying the user wants X amount of bunches from the
    instantaneous HR data. Realbunches is a the instantaneous heart rate array
    truncated to go to "groupnum" amount of bunched sets.

    :param mins: minutes
    :param rawbunches: raw instantaneous heart rate data
    :param update_time: windowing (seconds)
    :type update_time: int
    :type mins: str (from user)
    :type rawbunches: list
    :return: realbunches - truncated instantaneous heart rate data set
    :return: groupnum - number of groups to take out of the raw inst HR set
    :rtype realbunches: list
    :rtype groupnum: int

    """
    # Taking input and converting it to seconds
    if isinstance(mins, float) is True or isinstance(mins, int) is True:
        mins = mins
    elif isinstance(mins, complex) is True:
        raise ValueError('Please use real numbers.')

    # Conversion of minutes to seconds
    usersec = mins * min2sec

    # Must have number of groups be whole
    if usersec % update_time == 0:
        groupnum = int(usersec/update_time)
    # Taking an additional groups if user input is between groups
    else:
        groupnum = int(math.floor(usersec/update_time) + 1)

    # Take Niranjana's grouping output and truncating to fit user input
    # rawbunches = [80, 79, 85, 90, 77, 73]  # test data, should be inst_hr()
    if len(rawbunches) <= groupnum:  # if user time is > data indices
        realbunches = rawbunches
    else:
        realbunches = rawbunches[0:groupnum]
    return realbunches, groupnum


def avg_hr(realbunches, groupnum):
    """ returns avghr

    This function takes in the outputs of new_hr_set to get the
    averaged HR over the user specified amount of time.

    :param realbunches: Truncated inst HR data set
    :param groupnum: # of groups
    :type realbunches: list
    :type groupnum: int
    :return avghr: The average HR over the amount of time (min)
    specified by the user
    :rtype avghr: float, int

    """
    avghr = math.floor(sum(realbunches)/groupnum)
    return avghr
