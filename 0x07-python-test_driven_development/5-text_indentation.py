#!/usr/bin/python3
"""project 0x07 
contains:
functions
tests
"""

def text_indentation(text):
    '''size : int
    size of the square
    print the square'''
    
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    chars = "?.:"
    ss = text.strip(" ")
    n =""
    i = 0
    while i < len(ss):
        if (ss[i] == " " and n[-1] == "\n"):
            ""
        else:
            n += ss[i]
        if ss[i] in chars:
            n += "\n\n"
        i += 1

    print(n)