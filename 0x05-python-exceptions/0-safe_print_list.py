#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """ a counter to count printing elements"""
    counter = 0
    for element in range(x):
        try:
            """ using end because print add a new line """
            """ at the end of the execution by default """
            """ so we replace the default to print the """
            """ the whole loop's output on the same line """
            print("{}".format(my_list[element]), end="")
            counter += 1
            """break the loop if i passed an integer > len of my_list"""
            """ acting as a safe guard against accessing memory """
            """ out of list boundary """
        except IndexError:
            break
    print("")
    return counter
