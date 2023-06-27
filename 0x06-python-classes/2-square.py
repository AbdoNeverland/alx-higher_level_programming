#!/usr/bin/python3

""" create a class Square """


class Square:
    """ a square"""
    __size = 0

    def __init__(self, size=0):
        " init "
        try:
            self.__size = int(size)
            if size < 0:
                raise ValueError("size must be >= 0")
        except TypeError:
            raise TypeError("size must be an integer")
