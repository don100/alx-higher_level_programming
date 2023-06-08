#!/usr/bin/python3
char = ''
for a in range(122, 96, -1):
    char = chr(a) if a % 2 == 0 else chr(a-32)
    print("{}".format(char), end='')
