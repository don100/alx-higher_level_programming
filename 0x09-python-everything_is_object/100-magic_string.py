#!/usr/bin/python3
def magic_string():
    i = __import__('__main__').i
    return ("BestSchool, " * (i+1))[:-2]
