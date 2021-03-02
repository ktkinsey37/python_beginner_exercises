def sum_range(nums, start=0, end=None):
    """Takes an input list of nums, an index to begin, and an index to end.
    Sums all the nums in that list and outputs them.
    """
    output = 0
    i = start
    if type(end) != int:
        end = len(nums) - 1
    if end > len(nums) - 1:
        end = len(nums) - 1
    while i <= end:
        output += nums[i]
        i += 1
    return output