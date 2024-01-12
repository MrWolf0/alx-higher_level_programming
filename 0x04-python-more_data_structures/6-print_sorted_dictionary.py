#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    # cast the return valus in a list object
    # using formate of k:value that why we used {}:{}
    # sorted function sort the dictionary
    [print("{}: {}".format(k, a_dictionary[k])) for k in sorted(a_dictionary)]