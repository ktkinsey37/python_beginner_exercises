def valid_parentheses(parens):
    """Iterates through a string of parentheses to determine if they are all valid parens.
    """
    open_parens_true = 0
    start = 0
    if (len(parens) % 2 != 0):
        return False
    for paren in parens:
        if paren == "(":
            open_parens_true += 1
        if paren == ")":
            open_parens_true -= 1
            if open_parens_true < 0:
                return False
    if open_parens_true == 0:
        return True
    return False