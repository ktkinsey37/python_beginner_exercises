def intersection(l1, l2):
    """Returns intersection of two lists.
    Conversts lists to sets, finds intersection of sets, returns that as a list.
    """
    s1=set(l1)
    s2=set(l2)
    output = list(s1.intersection(s2))
    return output