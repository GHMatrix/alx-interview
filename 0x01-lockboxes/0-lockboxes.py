#!/usr/bin/python3
"""
Lockboxes
"""

from typing import List


def canUnlockAll(boxes: List[List[int]]) -> bool:
    """
    Determine if all the boxes can be opened.

    Args:
        boxes (List[List[int]]): A list of lists where each
        inner list represents a box
        and contains positive integers as keys.

    Returns:
        bool: True if all boxes can be opened, False otherwise.

    Notes:
        A key with the same number as a box opens that box.
        The first box (boxes[0]) is unlocked.

    Example:
        >>> boxes = [[1], [2], [3], [4], []]
        >>> canUnlockAll(boxes)
        True

        >>> boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
        >>> canUnlockAll(boxes)
        True

        >>> boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
        >>> canUnlockAll(boxes)
        False
    """
    if not boxes or not boxes[0]:
        return False

    n = len(boxes)
    visited = [False] * n
    visited[0] = True
    stack = [0]

    while stack:
        current_box = stack.pop()

        for key in boxes[current_box]:
            if 0 <= key < n and not visited[key]:
                visited[key] = True
                stack.append(key)

    return all(visited)


if __name__ == "__main__":
    # Example test case
    test_boxes = [[1, 2], [3], [0], []]
    print(canUnlockAll(test_boxes))
