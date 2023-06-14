#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary == None or len(a_dictionary) == 0:
        return None
    top = [list(a_dictionary.keys())[0], list(a_dictionary.values())[0]]
    for k, v in a_dictionary.items():
        top = [k, v] if v > top[1] else top
    return top[0]
