#!/usr/bin/python3
"""
Calculates the fewest number of operations needed to result
in exactly n H characters in the file.
"""


def minOperations(n):
    """
    Calculates the fewest number of operations needed to result
    in exactly n H characters in the file.

    :param n: integer, target number of H characters
    :return: integer, fewest number of operations needed
    """

    if n <= 1:
        return 0  # No operations needed for 0 or 1 H characters

    operations = 0
    i = 2  # Start from 2 since we have at least one H already in the file

    while i <= n:
        if n % i == 0:
            n //= i
            operations += i
        else:
            i += 1

    return operations


# Example usage
if __name__ == "__main__":
    n1 = 4
    print("Min number of operations to reach {} characters: {}".format(
        n1, minOperations(n1)))

    n2 = 12
    print("Min number of operations to reach {} characters: {}".format(
        n2, minOperations(n2)))
