#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    for i in range(0, int(len(my_list)/2)):
        x = my_list[i]
        my_list[i] = my_list[len(my_list)-1-i]
        my_list[len(my_list)-1-i] = x
    for i in range(0, len(my_list)):
        print("{:d}".format(my_list[i]))
