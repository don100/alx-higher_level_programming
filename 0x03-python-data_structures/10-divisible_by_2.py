#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    l = []
    for i in my_list:
        l.append(True if i % 2 == 0 else False)
    return l
