#!/usr/bin/python3
def remove_char_at(str, n):
    s = ''
    for a in range(0, len(str)):
        s += str[a] if a != n else ''
    return s
