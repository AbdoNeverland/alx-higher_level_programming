#!/usr/bin/python3
"""module"""


def add_attribute(cl, nm, vl):
    try:
        setattr(cl, nm, vl)
    except Exception as e:
        raise TypeError("can't add new attribute")
