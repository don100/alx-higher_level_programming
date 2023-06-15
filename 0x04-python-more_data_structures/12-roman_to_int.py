#!/usr/bin/python3
def roman_to_int(roman_string):
    romans = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    number = 0
    if type(roman_string) != str or roman_string == None:
        return number
    for i in range(len(roman_string)):
        if roman_string[i] == 'I' and i < len(roman_string) - 1 and roman_string[i+1] in ('V', 'X'):
            number -= 1
        else:
            number += romans[roman_string[i]]
    return number
