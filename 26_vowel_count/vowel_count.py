def vowel_count(phrase):
    """Iterates through an input string (phrase) and if that letter is a vowel,
    tracks its count in a dictionary. Returns a dict of vowels and their frequencies.
    """
    phrase = phrase.lower()
    vowels = 'aeiou'
    output = {}
    for letter in phrase:
        if letter in vowels:
            if letter in output:
                output[letter] += 1
            else:
                output[letter] = 0
    return output
