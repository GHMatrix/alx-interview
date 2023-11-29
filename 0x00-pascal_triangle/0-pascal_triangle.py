#!/usr/bin/python3
"""
Pascal Triangle
"""


def pascal_triangle(n):
    """
    Generate Pascal's triangle up to the specified number of rows.

    Args:
    - n (int): The number of rows in Pascal's triangle.

    Returns:
    - List[List[int]]: A list of lists of integers
    representing Pascal's triangle.

    Note:
    - Returns an empty list if n is less than or equal to 0.
    """
    if n <= 0:
        return []

    triangle = [[1]]
    for i in range(1, n):
        prev_row = triangle[i - 1]
        current_row = [1] + [prev_row[j - 1] + prev_row[j] for j in range(
            1, i)] + [1]
        triangle.append(current_row)

    return triangle


# Test the function
if __name__ == "__main__":
    triangle = pascal_triangle(5)
    for row in triangle:
        print("[{}]".format(",".join(map(str, row))))
