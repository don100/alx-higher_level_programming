#!/usr/bin/python3
def roman_to_int(roman_string):
    romans = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    number = 0
    if type(roman_string) != str or roman_string is None:
        return number
    r = roman_string
    for i in range(len(r)):
        if r[i] == 'I' and i < len(r) - 1 and r[i+1] in ('V', 'X'):
            number -= 1
        else:
            number += romans[r[i]]
    return number
