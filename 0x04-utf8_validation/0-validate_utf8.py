#!/usr/bin/python3
"""Defines the validUTF8 function"""


def validUTF8(data):
    """Checks if a given dataset represents a valid UTF8 encoding

    Args:
        data (List[int]): List of integers

    Returns:
        bool: returns true if the given dataset is valid UTF8, else false
    """

    byte_count = 0

    for i in data:
        if byte_count == 0:
            if i >> 5 == 0b110 or i >> 5 == 0b1110:
                byte_count = 1
            elif i >> 4 == 0b1110:
                byte_count = 2
            elif i >> 3 == 0b11110:
                byte_count = 3
            elif i >> 7 == 0b1:
                return False
        else:
            if i >> 6 != 0b10:
                return False
            byte_count -= 1
    return byte_count == 0
