#!/usr/bin/python3
def element_at(my_list, idx):
    # Check if idx is negative
    if idx < 0:
        return None

    # Check if idx is within the range of the list
    if idx < len(my_list):
        return my_list[idx]

    # Return None if idx is out of range
    return None