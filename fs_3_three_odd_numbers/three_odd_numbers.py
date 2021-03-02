def three_odd_numbers(nums):
    """Checks through the list nums looking for a sequence of three numbers that
    adds up to an odd number. Returns True/False based on if the sequence is found.
    """
    i = 0
    while i < (len(nums) - 2):
        if (nums[i] + nums[i+1] + nums[i+2]) % 2 != 0:
            return True
        i += 1
    return False