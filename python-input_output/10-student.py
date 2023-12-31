#!/usr/bin/python3
""" Student module
"""


class Student:
    """ Student class
    """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            return self.__dict__
        """ retrives common attributes to the list and the dict """
        new_dict = {}
        for attr in self.__dict__.keys():
            if attr in attrs:
                new_dict[attr] = self.__dict__[attr]
        return new_dict
