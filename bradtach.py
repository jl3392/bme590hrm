# Import necessary dependencies
# from avg_hr import avg_hr

# Initializing variables
bradythreshold = 60  # For normal adults
tachythreshold = 100  # For normal adults


def bradtach(avg_hr, tachythreshold, bradythreshold):
    if bradythreshold < avg_hr < tachythreshold:
        status = 2
    elif avg_hr >= tachythreshold:
        status = 1
    elif avg_hr <= bradythreshold:
        status = 0

    return status

