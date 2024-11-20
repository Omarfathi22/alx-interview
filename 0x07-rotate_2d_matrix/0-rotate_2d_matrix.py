#!/usr/bin/python3
"""
Rotate 2D Matrix
Given an n x n 2D matrix, rotate it 90 degrees clockwise in place.
"""


def transpose_matrix(matrix, n):
    """
    Rotates a 2D matrix 90 degrees clockwise in place.

    Args:
                    matrix (_type_): _description_
    """
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


def reverse_matrix(matrix):
    """_summary_

    Args:
                    matrix (_type_): _description_
    """
    for row in matrix:
        row.reverse()


def rotate_2d_matrix(matrix):
    """_summary_

    Args:
                    matrix (_type_): _description_
    """
    n = len(matrix)
    # print(n)

    """sample matrix
    1 2 3
    4 5 6
    7 8 9
    """

    # transpose matrix
    """
    1 4 7
    2 5 8
    3 6 9
    """

    transpose_matrix(matrix, n)

    # reverse matrix
    """
    7 4 1
    8 5 2
    9 6 3
    """
    reverse_matrix(matrix)

    return matrix
