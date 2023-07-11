#!/usr/bin/python3
"""100-my_int.py"""


class MyInt(int):
    """class MyInt"""

    def __eq__(self, other):
        return not (int(self) == other)
