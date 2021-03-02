def min_max_keys(d):
    """Accepts a dict as input, compares the keys to each other and returns
    a tuple of smallest and largest keys. Works for strings and ints.
    """
    key_list = []
    for key in d:
        key_list.append(key)

    if type(key[0]) == str:
        min = 'zzzz'
        max = ''
    else:
        max = 0
        min = key_list[0]

    for key in key_list:
        if key > max:
            max = key
    for key in key_list:
        if key < min:
            min = key
    return (min, max)