#!/usr/bin/python3
"""
     check object is an instance of specified class
     or object is an instance of child class of specifid class
"""


def is_kind_of_class(obj, a_class):
    """ obj is same class as a_class or same class of child class """
    return isinstance(obj, a_class)
