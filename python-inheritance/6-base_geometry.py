#!/usr/bin/python3
""" defines a class with public instance method area"""


class BaseGeometry:
    """ class named BaseGeometry with public instance method """
    def area(self):
        """ raise an exception """
        raise Exception("area() is not implemented")
