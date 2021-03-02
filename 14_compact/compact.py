def compact(lst):
    """Returns a copy of lst with non-true elements removed.
    Iterates through original list, asks if a boolean of the item is True,
    if so, appends to a new_list and outputs the new_list.
    """
    new_list = []
    for item in lst:
        if bool(item) == True:
            new_list.append(item)
    return new_list