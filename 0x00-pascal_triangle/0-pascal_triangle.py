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
        List of lists representing the triangle.
    """
    if n <= 0:
        return []

    # First row is always [1]
    triangle = [[1]]

    for i in range(1, n):
        # Start each row with a 1
        row = [1]
        
        # Each element is the sum of the two elements above it
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        
        # End each row with a 1
        row.append(1)
        
        # Add the row to the triangle
        triangle.append(row)

    return triangle

