#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    # use the first two elements of each tuple or 0 if not present
    # we take the first two elements of each tuple using
    # slicing notation [:2].
    # if the tuple has fewer than two elements
    # this will take all available elements
    # then we concatenate (0, 0) to ensure that tuple
    # always has at least two elements.
    # if tuple has more than two elements
    # only the first two will be considered.
    a = tuple_a[:2] + (0, 0)
    b = tuple_b[:2] + (0, 0)

    # Perform element-wise addition and return the result as a tuple
    result = (a[0] + b[0], a[1] + b[1])
    return result
