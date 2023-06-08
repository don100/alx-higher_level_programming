#!/usr/bin/python3
def fizzbuzz():
    str = ''
    for a in range(1, 101):
        if a % 3 != 0 and a % 5 != 0:
            str += f"{a} "
            continue
        if a % 3 == 0:
            str += "Fizz"
        if a % 5 == 0:
            str += "Buzz"
        str += ' '
    print(str, end='')
