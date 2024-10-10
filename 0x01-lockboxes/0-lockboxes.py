#!/usr/bin/python3
"""
Module for unlocking boxes.
"""

def canUnlockAll(boxes):
    """
    Determine if all boxes can be opened.

    Args:
        boxes (list of list): A list where each element represents a box
                               and contains the keys to other boxes.

    Returns:
        bool: True if all boxes can be opened, False otherwise.
    """
    n = len(boxes)  # Number of boxes
    unlocked = [False] * n  # Track which boxes have been unlocked
    unlocked[0] = True  # The first box is unlocked
    keys = boxes[0]  # Keys from the first box
    index = 0  # Index for processing boxes

    # Iterate while there are keys to process
    while index < n:
        if unlocked[index]:
            for key in boxes[index]:
                if key < n and not unlocked[key]:  # Check if key is valid
                    unlocked[key] = True  # Unlock the box
            index += 1  # Move to the next box
        else:
            index += 1  # Continue to next box

    return all(unlocked)  # Check if all boxes are unlocked

