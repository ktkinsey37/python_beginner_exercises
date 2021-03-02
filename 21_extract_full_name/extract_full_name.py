def extract_full_names(people):
    """For an input list of people (dictionaries with {first: first_name, last: last_name}),
    goes through the list of people and appends their full names to an output list.
    Returns the list.
    """
    output = []
    for person in people:
        full_name = person['first'] + f" {person['last']}"
        output.append(full_name)
    return output