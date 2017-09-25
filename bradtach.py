# Import necessary dependencies
# from avg_hr import avg_hr

"""
This module contains a function to tell a user whether or not they have a normal resting heart rate,
tachycardia, or bradycardia. It depends on initialized variables that will determine which thresholds to use
in determining the aforementioned indications.
"""



# Initializing variables
bradythreshold = 60  # For normal adults
tachythreshold = 100  # For normal adults


def bradtach(avghr, mins):
    """ returns status

    This function takes avghr from the avg_hr.py module and returns a status of 0,1,2. Each number corresponds with
    either normal RHR, bradycardia, or tachycardia.

    :param avghr: Average Heart Rate
    :param mins: User specified minutes
    :type avghr: int, float
    :param mins: float
    :return status: Condition of patient in numerical form
    :rtype status: int
    """
    if bradythreshold < avghr < tachythreshold:
        status = [2, 'You have a normal average heart rate over the period of {} minutes'.format(mins)]  # Normal
    elif avghr >= tachythreshold:
        status = [1, 'You have tachycardia over the period of {} minutes'.format(mins)]  # Tachycardia
    elif avghr <= bradythreshold:
        status = [0, 'You have bradycardia over the period of {} minutes'.format(mins)]  # Bradycardia

    return status

