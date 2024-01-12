#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum = 0
    # the set object contain only the unique values.
    for counter in set(my_list):
        sum += counter
    return sum
