def is_palindrome(phrase):
    """Checks if input phrase (str) is a palindrome or not.
    Capitalizes input phrase and removes spaces before
    checking if input phrase is same forwards and backwards.
    """
    phrase = phrase.upper()
    phrase = phrase.replace(' ', '')
    if phrase == phrase[::-1]:
        return True
    else:
        return False