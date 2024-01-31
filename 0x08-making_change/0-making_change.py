#!/usr/bin/python3
"""
Module for making change with the fewest coins
"""


def makeChange(coins, total):
    """
    Returns the fewest number of coins needed to meet the total
    """
    if total <= 0:
        return 0

    # Initialize a list to store the fewest number of coins for each total
    dp = [float('inf')] * (total + 1)

    # Base case: 0 coins needed for total 0
    dp[0] = 0

    # Iterate through each coin value
    for coin in coins:
        # Update dp array for each total value based on current coin
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1


if __name__ == "__main__":
    print(makeChange([1, 2, 25], 37))  # Output: 7
    print(makeChange([1256, 54, 48, 16, 102], 1453))  # Output: -1
