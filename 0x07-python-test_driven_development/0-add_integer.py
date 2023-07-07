#!/usr/bin/python3
'''Prototype: def add_integer(a, b=98):
a and b must be integers or floats
a and b must be first casted to
Returns an integer: the addition of a and b
You are not allowed to import '''
def add_integer(a, b=98):
    '''Prototype: def add_integer(a, b=98):
    a and b must be integers or floats,
    a and b must be first casted to '''
    if type(a) != int and type(a) != float:
        raise TypeError("a must be an integer")
    if type(b) != int and type(b) != float:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
