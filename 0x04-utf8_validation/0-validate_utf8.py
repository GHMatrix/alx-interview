#!/usr/bin/python3
"""
Determines if a given data set represents a valid UTF-8 encoding.
"""


def validUTF8(data):
    """
    Validates if a given data set is a valid UTF-8 encoding.

    Args:
        data (list): List of integers representing 1 byte of data each.

    Returns:
        bool: True if data is a valid UTF-8 encoding, else False.
    """
    num_bytes = 0

    mask_1 = 1 << 7
    mask_2 = 1 << 6

    for num in data:

        mask_byte = 1 << 7

        if num_bytes == 0:

            while mask_byte & num:
                num_bytes += 1
                mask_byte = mask_byte >> 1

            if num_bytes == 0:
                continue

            if num_bytes == 1 or num_bytes > 4:
                return False

        else:
            if not (num & mask_1 and not (num & mask_2)):
                return False

        num_bytes -= 1

    if num_bytes == 0:
        return True

    return False
