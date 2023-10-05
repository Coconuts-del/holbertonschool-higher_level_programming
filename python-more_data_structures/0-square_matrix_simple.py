#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    return ([list(map(lambda x: x ** 2, row)) for row in matrix])
    """ or with nested loops
    matrix_square = []
    for i in range(len(matrix)):
        matrix_row = []
        for j in range(len(matrix[i])):
            matrix_row.append(matrix[i][j] ** 2)
        matrix_square.append(matrix_row)
    return (matrix_square)"""
