#!/usr/bin/python3
"""
Module for unlocking boxes.
"""

from functools import reduce


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

    # Use a set to track keys we can use to unlock boxes
    keys_to_process = set(keys)

    # Process keys until we can't find new ones
    while keys_to_process:
        # Unlock boxes with the current keys
        current_key = keys_to_process.pop()
        if current_key < n and not unlocked[current_key]:
            unlocked[current_key] = True
            keys_to_process.update(boxes[current_key])  # Add new keys

    return all(unlocked)  # Check if all boxes are unlocked

