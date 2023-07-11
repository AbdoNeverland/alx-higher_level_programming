#!/usr/bin/python3
""" module """


class Student:
    """ class """

    def __init__(self, first_name, last_name, age):
        """function init"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """function dict"""
        if isinstance(attrs, list):
            d = {}
            for i in attrs:
                if not isinstance(i, str):
                    return self.__dict__
                if hasattr(self, i):
                    d[i] = getattr(self, i)
            return d
        return self.__dict__

    def reload_from_json(self, json):
        """ fonction"""
        for i, j in json.items():
            setattr(self, i, j)
