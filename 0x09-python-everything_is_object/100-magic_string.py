#!/usr/bin/python3
def magic_string():
    i = int(getattr(__import__(__name__), 'i', 0))
    return ("BestSchool, " * (i+1))[:-2]
