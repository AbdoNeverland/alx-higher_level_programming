#!/usr/bin/python3
"""module """


def append_write(filename="", text=""):
    """ function """
    nb = 0
    with open(filename, "a", encoding="utf-8") as f:
        nb = f.write(text)
        f.close()
    return nb
