#!/usr/bin/python3
"""module"""


def add_attribute(cl, nm, vl):
    """add """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(cl, nm, vl)
