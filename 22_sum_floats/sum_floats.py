def sum_floats(nums):
    """Loops through a list of nums and if their type is float, adds them.
    Returns the sum.
    """
    output = 0
    for num in nums:
        if type(num) == float:
            output = output + num
    return output
