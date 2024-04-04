#!/usr/bin/python3
"""
Write a method that determines if a given data set represents
a valid UTF-8 encoding.

 * Prototype: def validUTF8(data)
 * Return: True if data is a valid UTF-8 encoding, else return False
 * A character in UTF-8 can be 1 to 4 bytes long
 * The data set can contain multiple characters
 * The data will be represented by a list of integers
 * Each integer represents 1 byte of data, therefore you only need
   to handle the 8 least significant bits of each integer
"""

from typing import List


def validUTF8(data: List[int]) -> bool:
    """
    function to check if a byte is a start byte of a
    UTF-8 character

    Argument:
        data-(list[int]) - list of integers
    """
    def aVal(x: int, val: int) -> bool:
        """Checks if it is a valid byte"""
        if val == 7:
            return x >> 7 == 0b0
        elif val == 5:
            return x >> 5 == 0b110
        elif val == 4:
            return x >> 4 == 0b1110
        else:
            return x >> 3 == 0b11110

    def is_start_byte(b: int) -> bool:
        """Checks if the start value is a byte"""
        isByte = aVal(b, 7) or aVal(b, 5) or aVal(b, 4) or aVal(b, 3)
        return isByte

    def is_continuation_byte(byte):
        """ Function to check if a byte is a continuation byte"""
        return (byte >> 6) == 0b10

    # Iterate through the list of bytes
    i = 0
    while i < len(data):
        byte = data[i]

        # Check if it's a start byte
        if not is_start_byte(byte):
            return False
        if aVal(byte, 7):
            length = 1
        elif aVal(byte, 5):
            length = 2
        elif aVal(byte, 4):
            length = 3
        elif aVal(byte, 3):
            length = 4
        else:
            return False

        # Check if there are enough bytes in the data
        if i + length > len(data):
            return False

        for j in range(1, length):
            if not is_continuation_byte(data[i + j]):
                return False
        i += length
    return True
