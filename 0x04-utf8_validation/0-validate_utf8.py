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

    for num in data:
        # Check if the current byte is a continuation byte
        if num_bytes == 0:
            if (num >> 7) == 0b0:
                continue
            elif (num >> 5) == 0b110:
                num_bytes = 1
            elif (num >> 4) == 0b1110:
                num_bytes = 2
            elif (num >> 3) == 0b11110:
                num_bytes = 3
            else:
                return False
        else:
            # Check if the current byte is a continuation byte
            if (num >> 6) != 0b10:
                return False
            num_bytes -= 1

    # Check if there are any incomplete multibyte characters
    return num_bytes == 0
