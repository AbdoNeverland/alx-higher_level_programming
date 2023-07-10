#!/usr/bin/python3
"""module"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """class"""

    def __init__(self, size):
        """init"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """area"""
        return self.__size * self.__size
    def __str__(self):
        """str"""
        return f"[Square] {self.__width}/{self.__height}"    
