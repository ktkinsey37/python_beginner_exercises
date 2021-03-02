def find_the_duplicate(nums):
    """Finds a duplicate in a list but creating a set.
    Compares each num in the list to the set and if it's in there, returns True;
    if it's not, puts that number into the set.
    """
    i = 0
    set_of_nums = set()
    for num in nums:
        if num in set_of_nums:
            return num
        else:
            set_of_nums.add(num)
    return None
