#!/usr/bin/python3
"""class Student"""


class Student:
    """class"""

    def __init__(self, first_name, last_name, age):
        self.last_name = last_name
        self.first_name = first_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is not None:
            mydict = {}
            for i in self.__dict__.keys():
                if i in attrs:
                    mydict[i] = self.__dict__.get(i)
            return mydict
        else:
            return self.__dict__

    def reload_from_json(self, json):
        if json is not None:
            for i, j in json.items():
                setattr(self, i, j)
