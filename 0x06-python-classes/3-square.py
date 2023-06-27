#!/usr/bin/python3

""" create a class Square """


class Square:
    """ a square"""
    __size = 0

    def __init__(self, size=0):
        " init "
        if isinstance(size, int):
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size
        else:
            raise TypeError("size must be an integer")

    def area(self):
        return __size * __size
