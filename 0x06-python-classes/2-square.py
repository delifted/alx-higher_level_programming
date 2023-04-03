#!/usr/bin/python3
# py file by me
"""Class Square

   Empty Class"""


class Square:
    """Defines a Square"""
    def __init__(self, size=0):
        """Initializing Square Size"""
        try:
            self.__size = int(size)
            if size < 0:
                print("Size must be >= 0")
        except TypeError:
            print("Size must be an Integer")

