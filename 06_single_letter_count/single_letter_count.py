def single_letter_count(word, letter):
    """Counts the occurrences of an input letter inside of an input word.
    Achieves this by initializing count to 0 and using a forin loop and comparing to the letter and the uppercase letter.
    If it's a match, count adds 1.
    Returns count.
    """
    count = 0
    for char in word:
        if char == letter or char == letter.upper():
            count += 1
    return count