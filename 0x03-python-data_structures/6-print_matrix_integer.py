#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    # iterate through the rows
    for row in range(len(matrix)):
        # iterate through the columns
        for column in range(len(matrix[row])):
            # printing both row and column element such as
            # element row 1 and column 1
            print("{:d}".format(matrix[row][column]), end="")
            # if we reach the last column in each row remove the whitespace
            if column != (len(matrix[row]) - 1):
                print(" ", end="")

        print("")
