#!/usr/bin/python3
"""
Minimum Operations

This module contains a function to calculate the minimum number of operations
needed to achieve exactly n 'H' characters in a text file using only Copy All
and Paste operations.
"""


def minOperations(n):
    """
    Calculate the fewest number of operations needed to result in exactly n H characters.

    Parameters:
    n (int): The target number of H characters.

    Returns:
    int: Minimum number of operations needed, or 0 if impossible.
    """
    if n <= 1:
        return 0

    operations = 0
    current = 1
    factor = 1

    while current < n:
        if n % current == 0:  # If current is a factor of n
            operations += factor  # Perform Copy All (factor) operations
            factor = current      # Update factor to current
            current += factor     # Simulate the Paste operation
            operations += 1       # Count the Paste operation
        else:
            current += 1  # Increment current to try the next number

    return operations
