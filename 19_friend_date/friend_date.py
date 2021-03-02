def friend_date(a, b):
    """Compares through two friend tuplets, a and b.
    Loops through every item in a's hobby list and if it is also
    in b's hobby list, returns True. Else the function returns False.
    """


    for hobby in a[2]:
        if hobby in b[2]:
            return True
    return False