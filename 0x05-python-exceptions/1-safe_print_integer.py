#!/usr/bin/python3
def safe_print_integer(value):
    """ the using of TypeError and ValueError to handle
    the formatting and the value
    we must format the value into {:d} formate
    so using another value such as formate a str
    will case an error from incorrect data type
     and even the value is incorrect """
    try:
        print("{:d}".format(value))
        return True
    except (TypeError, ValueError):
        return False
