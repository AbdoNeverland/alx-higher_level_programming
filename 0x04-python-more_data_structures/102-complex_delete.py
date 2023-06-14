#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    ks = []
    for k, v in a_dictionary.items():
        if v == value:
            ks.append(k)
    for k in ks:
        if k in a_dictionary:
            del a_dictionary[k]
    return a_dictionary
