#!/usr/bin/python3
# py file by me
"""Class Square

   Empty Class"""


class Square:
    """Defines a Square"""
    def __init__(self, size=0):
        """Initializing Square Size"""
        if not isinstance(size, int):
            raise TypeError('Size must be an Integer')
        if size < 0:
            raise ValueError("Size must be >= 0")
        
        self.__size = size
