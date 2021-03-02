def list_check(lst):
    """Iterates through an input list and returns False if any item is not a list.
    Else returns True.
    """
    for item in lst:
        if type(item) != list:
            return False
    return True
