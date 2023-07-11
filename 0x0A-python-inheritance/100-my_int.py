#!/usr/bin/python3
"""100-my_int.py"""


class MyInt(int):
    """class MyInt"""

    def __eq__(self, other):
        return not(self == other)

    def __ne__(self, other):
        return not(self != other)

    def __lt__(self, other):
        return not(self < other)

    def __gt__(self, other):
        return not(self > other)

    def __le__(self, other):
        return not(self <= other)

    def __ge__(self, other):
        return not(self >= other)
