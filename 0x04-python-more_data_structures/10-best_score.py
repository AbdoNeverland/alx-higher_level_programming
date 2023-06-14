#!/usr/bin/python3
def best_score(a_dictionary):
    top = list(a_dictionary.values())[0]
    for k, v in a_dictionary.items():
        top = v if v > top else top
    return top
