#!/usr/bin/python3
def best_score(a_dictionary):
    if len(a_dictionary) == 0 or a_dictionary == None:
        return None
    top = list(a_dictionary.values())[0]
    for k, v in a_dictionary.items():
        top = v if v > top else top
    return top
