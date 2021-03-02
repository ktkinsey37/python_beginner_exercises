def reverse_vowels(s):
    """Loops through an input string (s) and creates a string of the vowels in it (excluding y).
    Then reverses the string of vowels and loops through the initial s again,
    replacing the normal vowels with the reversed vowels.
    """
    vowels_in_string = ''
    vowels = 'aeiouAEIOU'
    for letter in s:
        if letter in vowels:
            # capitalization throws an error
            vowels_in_string = vowels_in_string + letter
            vowels_reversed = vowels_in_string[::-1]
    count = 0
    for letter in s:
        if letter in vowels:
            letter = vowels_reversed[count]
        count += 1
    return s