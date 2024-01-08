#!/usr/bin/python3
def no_c(my_string):
    return_value = ""
    for letter in my_string:
        if letter != 'c' or letter != 'C':
            return_value += letter
    return return_value
