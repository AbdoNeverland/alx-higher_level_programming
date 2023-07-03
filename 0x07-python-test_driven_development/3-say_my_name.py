#!/usr/bin/python3
"""project 0x07 
contains:
functions
tests
"""

def say_my_name(first_name, last_name=""):
    '''first_name : str
    last_name : str
    print name'''
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")    
    print(f"My name is {first_name} {last_name}")
