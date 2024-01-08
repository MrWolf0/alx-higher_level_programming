#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    # first we will access only rows in matrix
    for row in matrix:
        # printing each index in row with a space between indices
        # using end argument
        for index in row:
            print("{:d}".format(index), end=" ")
        # print a new line
        print()
