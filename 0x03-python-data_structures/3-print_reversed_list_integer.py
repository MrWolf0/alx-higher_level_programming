#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    # checking my_list if it is a list object using isinstance.
    # if true it will reverse the list using builtin reverse fun.
    if isinstance(my_list, list):
        my_list.reverse()
        # printing the reversed list using formate function.
        for index in my_list:
            print("{:d}".format(index))
