#!/usr/bin/python3
"""project 0x07 
contains:
functions
tests
"""

def text_indentation(text):
    """ print lines after specific characters"""

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    characters = [".", "?", ":"]
    splitable = ""
    for nc in text:
        if nc in characters:
            splitable += nc
            splitable += "😀"
        else:
            splitable += nc

    lines = splitable.split("😀")
    incre = 0
    for line in lines:
        line = line.strip()
        print(line, end="")
        if incre != len(lines) - 1:
            print("\n\n", end="")
        incre += 1
