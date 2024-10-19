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
        
        if n % root == 0:
                
            ops += root
            
            n = n / root
            
            root -= 1
        
        root += 1
    return ops
