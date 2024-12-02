#!/usr/bin/python3
"""
Island Perimeter Problem:
This module contains the `island_perimeter` function that calculates
the perimeter of an island represented in a 2D grid.
"""

def island_perimeter(grid):
    """
    Calculate the perimeter of the island described in grid.
    
    Args:
        grid (list of list of int): A 2D grid where:
            - 0 represents water
            - 1 represents land
    """
    perimeter = 0  # Initialize perimeter count to 0
    
    # Iterate through each cell in the grid
    for i in range(len(grid)):  # Loop through rows
        for j in range(len(grid[i])):  # Loop through columns
            if grid[i][j] == 1:  # If the cell is land
                # Check the top neighbor
                if i == 0 or grid[i - 1][j] == 0:  # Either at grid boundary or water above
                    perimeter += 1
                # Check the bottom neighbor
                if i == len(grid) - 1 or grid[i + 1][j] == 0:  # Either at grid boundary or water below
                    perimeter += 1
                # Check the left neighbor
                if j == 0 or grid[i][j - 1] == 0:  # Either at grid boundary or water to the left
                    perimeter += 1
                # Check the right neighbor
                if j == len(grid[i]) - 1 or grid[i][j + 1] == 0:  # Either at grid boundary or water to the right
                    perimeter += 1
    
    return perimeter
