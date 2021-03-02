def weekday_name(day_of_week):
    """Returns the name of the weekday corresponding to an input number.
    Compares input number to weekdays list and outputs what is at that index minus 1.
    """
    weekdays = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    if day_of_week >= 1 and day_of_week <= 7:
        return weekdays[day_of_week - 1]
    else:
        return None