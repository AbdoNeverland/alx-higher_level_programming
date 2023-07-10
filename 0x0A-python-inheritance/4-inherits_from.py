#!/usr/bin/python3
"""module"""


def inherits_from(obj, a_class):
    """ is"""
    return type(obj) != a_class and issubclass(type(obj), a_class)
