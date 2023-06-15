#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    myKeys = list(a_dictionary.keys())
    myKeys.sort()
    for a in myKeys:
        print(f"{a}: {a_dictionary[a]}")
