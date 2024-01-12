#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    # map function used here to execute
    # the lambda expression on each row in matrix
    # lambda take argument which num and then do
    # the instruction after : which num*num.
    # map will execute the lambda expression each
    # time find a number in the matrix
    # finally we cast the output to list object
    return ([list(map(lambda num: num * num, row)) for row in matrix])
