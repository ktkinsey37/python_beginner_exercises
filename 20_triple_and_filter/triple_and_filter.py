def triple_and_filter(nums):
    """Goes through each number in the list and checks if it's divisible by 4.
    If it is, triples the number and appends it to the output list.
    """
    output = []
    for num in nums:
        if num % 4 == 0:
            output.append(num * 3)
    return output