#!/usr/bin/python3
"""class Student"""


class Student:
    """class"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        return self.__dict__

    def to_json(self, attrs=None):
        if attrs:
            mydict = {}
            for i in attrs:
                if i in self.__dict__.keys():
                    mydict[i] = self.__dict__.get(i)
            return mydict
        else:
            return self.__dict__
