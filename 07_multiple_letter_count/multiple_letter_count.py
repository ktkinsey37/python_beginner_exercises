def multiple_letter_count(phrase):
    """Takes an input string (phrase) and returns a dict of the letter frequencies.
    Capitals and lower-cases are considered different letters.
    """
    output = {}
    for letter in phrase:
        if letter not in output:
            output[f'{letter}'] = 0
        if letter in output:
            output[f'{letter}'] += 1
    return output