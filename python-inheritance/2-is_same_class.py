#!/usr/bin/python3
""" 
     check object is exactly an instance of the specified class
"""


def is_same_class(obj, a_class):
    """ return result of comparison : obj and a_class """
    return type(obj) is a_class
