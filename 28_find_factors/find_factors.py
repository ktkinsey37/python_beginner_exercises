def find_factors(num):
    """Finds the factors of an input num. Does this by iterating
    through a range between 1 and the num to identify factors.
    """
    output = []
    for i in range(1, num + 1):
        if num % i == 0:
            output.append(i)
    return output
