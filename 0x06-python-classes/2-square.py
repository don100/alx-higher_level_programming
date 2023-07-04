#!/usr/bin/python3
"""class Square"""


class Square:
    """Content class square."""
    def __init__(self, size=0):
        if type(size) != int:
            raise Exception("size must be an integer")
        if size < 0:
            raise Exception("size must be >= 0")
        self.__size = size
