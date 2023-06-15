#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    best = max(a_dictionary.values())
    best_key = [i for i in a_dictionary if a_dictionary[i] == best]
    return best_key[0] if best > 0 else None
