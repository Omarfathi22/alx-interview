#!/usr/bin/python3
"""N Queens placement on NxN chessboard"""

import sys


def generate_solutions(row, column):
    """
    Generate all possible solutions for placing queens on an NxN chessboard.

    Arguments:
    row -- Number of rows (queens) to place
    column -- Number of columns (board size)

    Returns:
    solution -- List of valid configurations (solutions) of queens' placements
    """
    solution = []
    for queen in range(row):
        solution = place_queen(queen, column, solution)
    return solution


def place_queen(queen, column, prev_solution):
    """
    Place a queen in a valid position in the given row.

    Arguments:
    queen -- Current row to place the queen
    column -- Total number of columns
    prev_solution -- List of already placed queens' positions

    Returns:
    safe_position -- List of all valid positions for the current queen
    """
    safe_position = []
    for array in prev_solution:
        for x in range(column):
            if is_safe(queen, x, array):
                safe_position.append(array + [x])
    return safe_position


def is_safe(q, x, array):
    """
    Check if placing a queen at position (q, x) is safe.
    A position is safe if no queen already placed can attack the new position.

    Arguments:
    q -- Row index of the new queen
    x -- Column index of the new queen
    array -- List of positions of already placed queens

    Returns:
    True if the position (q, x) is safe, False otherwise
    """
    if x in array:
        return False
    else:
        return all(abs(array[column] - x) != q - column for column in range(q))


def init():
    """
    Initialize and validate the input argument (N) from the command line.

    Returns:
    n -- The size of the chessboard (N)

    Exits with status 1 if the input is invalid
    (not a number, less than 4, or missing).
    """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if sys.argv[1].isdigit():
        n = int(sys.argv[1])
    else:
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    return n


def n_queens():
    """
    Main function to solve the N-Queens problem and print all valid solutions.
    """
    n = init()
    solutions = generate_solutions(n, n)

    for array in solutions:
        clean = []
        for q, x in enumerate(array):
            clean.append([q, x])
        print(clean)


if __name__ == "__main__":
    n_queens()
