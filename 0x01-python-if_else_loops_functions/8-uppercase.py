#!/usr/bin/python3
def uppercase(str):
    s = ""
    for c in str:
            s += chr(ord(c)-32) if ord(c) >= 97 and ord(c) <= 123 else c
    print("{}".format(s))
