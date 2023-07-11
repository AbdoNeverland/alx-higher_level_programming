#!/usr/bin/python3
"""module """


def read_file(filename=""):
    """ function """
    f = open(filename, "r")
    print(f.read())
    f.close()

