#!/usr/bin/python3
""" module """


def append_after(filename="", search_string="", new_string=""):
    """fonction"""
    ss = ""
    with open(filename, "r") as f:
        for ln in f:
            ss += ln
            if search_string in ln:
                ss += new_string
        f.close()
    with open(filename, "w") as f:
        f.write(ss)
        f.close()
