def same_frequency(num1, num2):
    """Takes two input ints and returns True if they have the same fequency of integers.
    """
    if sorted(list(str(num1))) == sorted(list(str(num2))):
        return True
    return False