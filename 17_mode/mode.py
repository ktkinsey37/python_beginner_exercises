def mode(nums):
    """Return the most-common number in the list.
    Creates a dictionary with key value pairs for numbers:frequency.
    Then figures out which number has the highest frequency and outputs that number.
    """
    output = {}
    for num in nums:
        if num in output:
            output[num] += 1
        else:
            output[num] = 0
    mode_val = 0
    mode_count = 0
    for k in output:
        if output[k] > mode_count:
            mode_val = k
            mode_count = output[k]
    return mode_val