#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    counter = 0
    for element in range(x):
        try:
            print("{:d}".format(my_list[element]), end="")
            counter += 1
            """ if there is any error in type of data or its """
            """ value throw an exception and  continue the execution """
        except(TypeError, ValueError):
            continue
    print("")
    return counter
