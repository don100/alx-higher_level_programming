#!/usr/bin/python3
if __name__ != "__main__":
    exit()
from sys import argv
if len(argv) != 4:
    print("Usage: ./100-my_calculator.py <a> <operator> <b>")
    exit(1)
elif argv[2] not in ('+', '-', '*', '/'):
    print("Unknown operator. Available operators: +, -, * and /")
    exit(1)
else:
    x = 0
    match argv[2]:
        case "+":
            x = add(int(argv[1]), int(argv[3]))
        case "-":
            x = sub(int(argv[1]), int(argv[3]))
        case "*":
            x = mul(int(argv[1]), int(argv[3]))
        case "/":
            x = div(int(argv[1]), int(argv[3]))
    
    print("{} {} {} = {}".format(int(argv[1]), argv[2], int(argv[3]), x))
    exit(0)
