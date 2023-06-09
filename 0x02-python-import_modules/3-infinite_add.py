#!/usr/bin/python3
if __name__ != "__main__":
    exit()
from sys import argv
s = 0
for a in argv[1:]:
    s+=a
print(s)
