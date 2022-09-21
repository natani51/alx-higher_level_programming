#!/usr/bin/python3

"""Documentation for a simple division function"""


def matrix_divided(matrix, div):
    msg = "matrix must be a matrix (list of lists) of integers floats"
    msg2 = "dividion by zero"
    msg3 = "div must be a number"
    msg4 = "Each row of the matrix must have the same size"

    if matrix == None:
        raise TypeError(msg)
    if len(matrix) == 0:
        raise TypeError(msg)
    if type(matrix) in [tuple, set]:
        raise TypeError(msg)
    for i in matrix:
        if len(i) == 0 or type(i) in [tuple, set]:
            raise TypeError(msg)
    if div == 0:
        raise ZeroDivisionError(msg2)
    if not isinstance(div, (int, float)):
        raise TypeError(msg3)
    leng = len(matrix[0])
    for j in matrix:
        if len(j) != leng:
            raise TypeError(msg4)
    for i in range (len(matrix)):
        for j in range(len(matrix[i])):
            if type(matrix[i][j]) not in [int, float]:
                raise TypeError(msg)
    new_matrix = [list(map(lambda x: round(x / div, 2), i)) for i in matrix]
    return new_matrix
