#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    myList = []
    for i in my_list:
        myList.append(True if i % 2 == 0 else False)
    return myList
