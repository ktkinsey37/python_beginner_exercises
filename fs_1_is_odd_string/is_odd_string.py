def is_odd_string(word):
    """Accepts a word as input. For every letter in the word,
    adds the letters place-value (a = 1, b = 2, c = 3, A = 1, etc.).
    If the sum of the letters' place-values is odd, returns True, else False.
    """
    output = 0
    for letter in word:
        output = output + ord(f'{letter}')
    if output == 1:
        return True
    if output % 2 == 0:
        return False
    else:
        return True


    # Hint: you may find the ord() function useful here