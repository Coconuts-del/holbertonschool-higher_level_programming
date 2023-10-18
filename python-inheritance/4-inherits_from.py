#!/usr/bin/python3
"""
     check object is an instance of subclass of specifid class
"""


def inherits_from(obj, a_class):
    """ obj is same class of subclass of a_class """
    if type(obj) is not a_class:
        return isinstance(obj, a_class)
    return False
