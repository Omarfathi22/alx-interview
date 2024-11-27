#!/usr/bin/python3

""" Contains makeChange function """

def makeChange(coins, total):
    """
    Returns: fewest number of coins needed to meet total
        If total is 0 or less, return 0
        If total cannot be met by any number of coins you have, return -1
    """
    # Check if coins list is empty or None, return -1 if so (i.e., no coins to make change)
    if not coins or coins is None:
        return -1
    
    # If total is 0 or less, no coins are needed, so return 0
    if total <= 0:
        return 0
    
    change = 0  # Variable to track the number of coins used
    coins = sorted(coins)[::-1]  # Sort the coins in descending order for optimal change-making

    # Loop through each coin type starting from the largest
    for coin in coins:
        # While the coin can be used (i.e., it is less than or equal to the remaining total)
        while coin <= total:
            total -= coin  # Subtract the coin value from total
            change += 1  # Increment the coin count
    
        # If the total reaches 0, we have successfully made the exact change
        if total == 0:
            return change
    
    # If the loop finishes and the total is not 0, it's not possible to make the exact change
    return -1
