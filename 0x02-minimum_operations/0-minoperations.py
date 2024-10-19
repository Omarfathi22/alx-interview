#!/usr/bin/python3
"""
Minimum Operations

This module contains a function to calculate the 
minimum number of operations
needed to achieve exactly n 'H' characters in a text
file using only Copy All
and Paste operations.
"""



def minOperations(n):
    """
    minOperations
    Gets fewest # of operations needed to
    result in exactly n H characters
    """
    
    
    if (n < 2):
        return 0
    ops, root = 0, 2
    while root <= n:
        # if n evenly divides by root
        if n % root == 0:
            # total even-divisions by root = total operations
            ops += root
            # set n to the remainder
            n = n / root
            # reduce root to find remaining smaller vals
            # that evenly-divide n
            root -= 1
        # increment root until it evenly-divides n
        root += 1
    return ops
