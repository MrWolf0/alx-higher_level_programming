#!/usr/bin/python3
def search_replace(my_list, search, replace):
    cp_list = my_list[:]
    for counter in range(len(cp_list)):
        if cp_list[counter] == search:
            cp_list[counter] = replace
    return cp_list
