#!/usr/bin/python3
"""9-rectangle.py"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """class Rectangle"""

    def __init__(self, width, height):
        self.integer_validator('width', width)
        self.__width = width
        self.integer_validator('height', height)
        self.__height = height

    def __str__(self):
        return "{} {}/{}".format(self.__class__.__name__,
                                 self.__size, self.__size)

    def area(self):
        return self.__width * self.__height
