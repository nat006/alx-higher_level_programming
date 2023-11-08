#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    square_matrix = []

    for i in range(len(matrix)):
        square_row = []

        for j in range(len(matrix[i])):
            square_value = matrix[i][j] ** 2
            square_row.append(square_value)

        square_matrix.append(square_row)

    return square_matrix
