#!/usr/bin/python3
''' 3-is_kind_of_class.py '''


def is_kind_of_class(obj, a_class):
    ''' is_kind_of_class '''
    return issubclass(type(obj), a_class)
