#!/usr/bin/python3
"""A module that defines a square"""


class Square:
    """Defines a Square"""

    def __init__(self, size=0):
        """Initializing Square Size
        Args:
            size: represents the size of the square definition
        Raises:
            TypeError: when size is not an integer
            ValueError: if size is less than zero
        """

        if not isinstance(size, int):
            raise TypeError('Size must be an Integer')
        if size < 0:
            raise ValueError("Size must be >= 0")

        self.__size = size
