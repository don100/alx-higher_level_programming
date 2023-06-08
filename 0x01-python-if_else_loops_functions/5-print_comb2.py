#!/usr/bin/python3
for a in range(0, 100):
    num = str(a) if a >= 10 else '0'+str(a)
    num += ", " if a < 99 else '\n'
    print("{0}".format(num), end='')
