#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for k, v in sorted(a_dictionary.items()):
        print(f"{k}: {v}")
def update_dictionary(a_dictionary, key, value):
    d = a_dictionary.copy()
    d[key] = value
    return d
