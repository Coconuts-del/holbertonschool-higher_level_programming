#!/usr/bin/python3
"""
  Divides all elements of a matrix by div rounded to 2 decimal places
  matrix must be a list of lists of integers or floats
  div must be a number (integer or float) and not equal to 0
  Each row of the matrix must be of the same size
  Return new matrix or raise Exception
"""


def matrix_divided(matrix, div):
    """ validation div """
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    """ validation matrix """
    if not matrix:
        raise TypeError("matrix must be a matrix (list of lists) "
                        "of integers/floats")
    lenrow = len(matrix[0])
    for row in matrix:
        if type(row) is not list:
            raise TypeError("matrix must be a matrix (list of lists) "
                            "of integers/floats")
        if len(row) != lenrow:
            raise TypeError("Each row of the matrix must have the same size")
        for item in row:
            if type(item) not in [int, float]:
                raise TypeError("matrix must be a matrix (list of lists) "
                                "of integers/floats")
    """ create new matrix """
    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
