def two_list_dictionary(keys, values):
    """Takes as input two lists and creates a dictionary of keys and values from them.
    If there is no key for the value, ignores the value. If there is no value for the key,
    provides a key of None. Outputs the dictionary.
   """
    output_dict = {}
    i = 0
    for key in keys:
        if i >= len(values):
            output_dict[key] = None
        else:
            output_dict[key] = values[i]
        i += 1
    return output_dict
