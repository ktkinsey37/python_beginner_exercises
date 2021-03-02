def flip_case(phrase, to_swap):
    """Accepts a letter, to_swap, and finds all instances of it in the input phrase.
    For each instance, swaps the case of the letter. Input disregards capitalization.
    """
    new_phrase = ''
    for char in phrase:
        if char == to_swap or char == to_swap.swapcase():
            char = char.swapcase()
            new_phrase = new_phrase + char
        else:
            new_phrase = new_phrase + char
    return new_phrase
