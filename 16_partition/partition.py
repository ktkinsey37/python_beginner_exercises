def partition(lst, fn):
    """Accepts a list and a function(which returns a boolean) as arguments.
    Runs the list through the function, then sorts into a true list and false list based on the results.
    Outputs a list of those two (true and false) lists.
    """
    output = []
    true_list = []
    false_list = []
    for item in lst:
        if fn(item) == True:
            true_list.append(item)
        elif fn(item) == False:
            false_list.append(item)
    output.append(true_list)
    output.append(false_list)
    return output