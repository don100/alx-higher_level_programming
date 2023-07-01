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

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise Exception("size must be an integer")
        if value < 0:
            raise Exception("size must be >= 0")
        self.__size = value

    def area(self):
        return self.__size*self.__size

    def __eq__(self, other):
        return self.area() == other.area()

    def __ne__(self, other):
        return self.area() != other.area()

    def __lt__(self, other):
        return self.area() < other.area()

    def __gt__(self, other):
        return self.area() > other.area()

    def __le__(self, other):
        return self.area() <= other.area()

    def __ge__(self, other):
        return self.area() >= other.area()
