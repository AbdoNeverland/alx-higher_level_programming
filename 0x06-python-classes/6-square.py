#!/usr/bin/python3

""" create a class Square """


class Square:
    """ a square"""
    __size = 0
    __position = (0, 0)

    def __init__(self, size=0, position=(0, 0)):
        " init "
        self.size = size
        self.position = position

    def area(self):
        return self.__size * self.__size

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if isinstance(value[0], int) and isinstance(value[1], int) and value[0] >= 0 and value[0] >= 0:
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if isinstance(value, int):
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value
        else:
            raise TypeError("size must be an integer")

    def my_print(self):
        for k in range(self.__position[1]):
            print("")
        for i in range(self.__size):
            for k in range(self.__position[0]):
                print("_", end="")
            for j in range(self.__size):
                print("#", end="")
            print()
        if self.__size == 0:
            print("")
