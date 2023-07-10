#!/usr/bin/python3
"""module"""


class BaseGeometry:
    """ base geo"""
    def area(self):
        """raise"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """des"""
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


