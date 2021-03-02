def find_greater_numbers(nums):
    """Finds and returns number of instances a number is succeeded in a list by a number greater than it.
    Does this by iterating through each index of list and starting there and comparing it with all the numbers
    that come after it.
    """
    output = 0
    i = 0
    while i < len(nums):
        j = i
        while j < len(nums):
            if nums[i] < nums[j]:
                output += 1
                print(output, i, j)
                j += 1
            else:
                j += 1
        i += 1
    return output