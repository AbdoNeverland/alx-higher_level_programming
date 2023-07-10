#!/usr/bin/python3
"""module"""


class MyInt(int):
    """class"""

    def __eq__(self, o):
        """d"""
        return self.real != o

    def __ne__(self, o):
        """d"""
        return self.real == o
