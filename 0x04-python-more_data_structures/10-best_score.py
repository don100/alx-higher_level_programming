#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary == None:
        return None
    best_key = [i for i in a_dictionary if a_dictionary[i]==max(a_dictionary.values())]
    return best_key[0]
