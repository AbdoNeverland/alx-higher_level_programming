#!/usr/bin/python3
"""function to add two integer
a : int or float
b : int or float
Return : a + b
"""

def matrix_divided(matrix, div):
    '''a : int or float
    b : int or float
    Return: addition of a and b'''
    e1 = "matrix must be a matrix (list of lists) of integers/floats"
    e2 = "Each row of the matrix must have the same size"
    if not isinstance(div, (int,float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError(e1)
    new_matrix = matrix.copy()
    for i, m in enumerate(matrix):
        if not isinstance(m, list):
            raise TypeError(e1)
        if i != 0 and len(m) != len(matrix[i-1]):
            raise TypeError(e2)
        new_matrix[i] = matrix[i].copy()
        for k, e in enumerate(m):
            if not isinstance(e, (int, float)):
                raise TypeError(e1)
            new_matrix[i][k] = round(new_matrix[i][k] / div, 2)
    return new_matrix