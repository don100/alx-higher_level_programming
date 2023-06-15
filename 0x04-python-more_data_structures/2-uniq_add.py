#!/usr/bin/python3
def uniq_add(my_list=[]):
    s = 0
    for i in set(my_list):
        s += i
    return s
'''
def uniq_add(my_list=[]):
    s = 0
    for i in range(len(my_list)):
        if my_list[i] not in my_list[i+1:]:
            s += my_list[i]
    return s
'''
