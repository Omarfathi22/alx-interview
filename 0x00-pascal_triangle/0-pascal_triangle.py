#!/usr/bin/python3
"""
This module contains the function pascal_triangle
which generates Pascal's Triangle up to n rows.
"""

def pascal_triangle(n):
    """
    Returns a list of lists representing Pascal's Triangle.

    Args:
        n (int): The number of rows of Pascal's Triangle.

    Returns:
        List of lists representing Pascal's Triangle.
        Returns an empty list if n <= 0.
    """
    if n <= 0:
        return []

    triangle = [[1]]  # The first row is always [1]

    for i in range(1, n):
        row = [1]  # Every row starts with 1
        for j in range(1, i):
            # Add the sum of the two elements directly above this element
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        row.append(1)  # Every row ends with 1
        triangle.append(row)

    return triangle

