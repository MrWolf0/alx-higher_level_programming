#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0 or idx >= len(my_list):
        return my_list
    # here we just copy all elements in my_list into new copy using :
    # mean access all elements in the list
    new_copy = my_list[:]
    new_copy[idx] = element
    return new_copy
