def two_oldest_ages(ages):
    """Scans through a tuple of ages and returns the first and second oldest ages.
    """
    oldest = 0
    second_oldest = 0
    ages = set(ages)
    for age in ages:
        if age > oldest:
            oldest = age
    for age in ages:
        if age != oldest and age > second_oldest:
            second_oldest = age
    return (second_oldest, oldest)
    # NOTE: don't worry about an optimized runtime here; it's fine if
    # you have a runtime worse than O(n)

    # NOTE: you can sort lists with lst.sort(), which works in place (mutates);
    # you may find it helpful to research the `sorted(iter)` function, which
    # can take *any* type of list-like-thing, and returns a new, sorted list
    # from it.