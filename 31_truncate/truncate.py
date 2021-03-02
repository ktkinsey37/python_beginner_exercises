def truncate(phrase, n):
    """A function that truncates the input phrase at the input number of char (n).
    If the user tries to truncate below three chars, throws an error.
    If the phrase to truncate is less than the num, returns the phrase.
    """
    output = ''
    if n < 3:
        return 'Truncation must be at least 3 characters.'
    else:
        num_to_concat_to = n - 3
        if len(phrase) < num_to_concat_to:
            return phrase
        i = 0
        while i < num_to_concat_to:
            output = output + phrase[i]
            i += 1
            print(output)
    return output + '...'