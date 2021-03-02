def multiply_even_numbers(nums):
    """Iterates through array and multiplies any even number times the initial newnum.
    """
    newnum = 1
    for num in nums:
        if num % 2 == 0:
            newnum = newnum * num
    return newnum