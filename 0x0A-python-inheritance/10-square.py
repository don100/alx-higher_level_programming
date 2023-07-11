#!/usr/bin/python3
"""10-square.py"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class Square"""

    def __init__(self, size):
        self.integer_validator('size', size)
        self.__size = size

    def __str__(self):
        s = "{} {}/{}".format(self.__class__.__name__,\
                              self.__size, self.__size)
        return s

    def area(self):
        return self.__size * self.__size
