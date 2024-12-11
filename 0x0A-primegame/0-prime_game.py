#!/usr/bin/python3
"""0. Prime Game - Maria and Ben are playing a game"""

def isWinner(x, nums):
    """
    Function to determine the winner of the Prime Game between Maria and Ben.

    Args:
    x (int): The number of rounds in the game.
    nums (list): A list of integers where each integer represents the number of turns in that round.

    Returns:
    str: "Ben" if Ben wins, "Maria" if Maria wins, or None if it's a tie or invalid input.
    """
    # Validate input
    if x <= 0 or nums is None:
        return None
    if x != len(nums):
        return None

    # Initialize scores for Ben and Maria
    ben = 0
    maria = 0

    # Create a list to mark prime numbers using Sieve of Eratosthenes
    a = [1 for _ in range(sorted(nums)[-1] + 1)]  # List to track prime numbers
    a[0], a[1] = 0, 0  # 0 and 1 are not primes

    # Sieve of Eratosthenes to mark non-primes (multiples of primes)
    for i in range(2, len(a)):
        rm_multiples(a, i)

    # Iterate through the rounds in nums to calculate the score
    for i in nums:
        # Check if the sum of primes up to the current number is even or odd
        if sum(a[0:i + 1]) % 2 == 0:
            ben += 1  # Ben scores if the sum is even
        else:
            maria += 1  # Maria scores if the sum is odd

    # Determine the winner based on who scored more
    if ben > maria:
        return "Ben"
    if maria > ben:
        return "Maria"
    return None  # Return None if there's a tie or no winner


def rm_multiples(ls, x):
    """
    Function to mark the multiples of a prime number as non-prime (0).

    Args:
    ls (list): The list tracking prime numbers.
    x (int): The current prime number whose multiples will be marked.
    """
    for i in range(2, len(ls)):
        try:
            ls[i * x] = 0  # Mark multiples of x as non-prime
        except (ValueError, IndexError):
            break  # Stop if index is out of range or if the value is invalid
