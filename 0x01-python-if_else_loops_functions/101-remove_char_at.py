#!/usr/bin/python3
def remove_char_at(str, n):
    ss = ""
    for i, c in enumerate(str):
        if (i != n):
            ss += c
    return (ss)
