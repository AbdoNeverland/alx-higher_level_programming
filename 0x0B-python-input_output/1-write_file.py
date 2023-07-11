#!/usr/bin/python3
"""module """


def write_file(filename="", text=""):
    """ function """
    nb = 0
    with open(filename, "w", encoding="utf-8") as f:
        nb = f.write(text)
        f.close()
    return nb
