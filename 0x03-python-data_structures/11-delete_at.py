#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    # Check if the index is within the valid range
    if 0 <= idx < len(my_list):
        # Create a new list excluding the element at the specified index
        new_list = my_list[:idx] + my_list[idx+1:]
        return new_list
    else:
        # If the index is negative or out of range, return the same list
        return my_list
