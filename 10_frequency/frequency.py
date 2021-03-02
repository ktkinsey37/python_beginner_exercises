def frequency(lst, search_term):
    """Iterates through input lst and compares that item to the search_term.
    If it is the same, increments count by 1. Afterwards, returns count.
    """
    count = 0
    for item in lst:
        if item == search_term:
            count += 1
    return count