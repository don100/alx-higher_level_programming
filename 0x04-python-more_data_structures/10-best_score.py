#!/usr/bin/python3
def best_score(a_dictionary):
    best_key = None
    best = ""
    if a_dictionary is None:
        return best_key
    best_key = 0
    for x, y in a_dictionary.items():
        if y > best_key:
            best_key = y
            best = x
    return best
