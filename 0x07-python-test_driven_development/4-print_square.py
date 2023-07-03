#!/usr/bin/python3
"""project 0x07 
contains:
functions
tests
"""

def print_square(size):
    '''size : int
    size of the square
    print the square'''
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")    
    print("\n".join(["#" * size] * size))
