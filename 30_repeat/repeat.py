def repeat(phrase, num):
    """Returns an input phrase an input num of times.
    Returns None if the integer is less than zero or not an integer.
    While a count is less than the input num, concatenates the output phrase with the input phrase.
    """
    count = 0
    new_phrase = ''
    if type(num) != int or num <= 0:
        return None
    while count < num:
        new_phrase = new_phrase + phrase
        count += 1
    return new_phrase
    