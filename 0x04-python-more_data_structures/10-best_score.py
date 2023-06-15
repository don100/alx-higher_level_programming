#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return "None"
    else:
        best_key = 0
        best = ""
        for x, y in a_dictionary.items():
            if y > best_key:
                best_key = y
                best = x
        return best if best_key != 0 else None
