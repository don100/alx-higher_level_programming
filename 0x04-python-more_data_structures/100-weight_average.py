#!/usr/bin/python3
def weight_average(my_list=[]):
    a = sum(map(lambda x: x[0]*x[1], my_list))
    b = sum(map(lambda x: x[1], my_list))
    result = a/b
    return result
