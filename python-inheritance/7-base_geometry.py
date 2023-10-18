#!/usr/bin/python3
""" defines a class with public instance method area"""


class BaseGeometry:
    """ class named BaseGeometry with public instance method """
    def area(self):
        """ raise an exception """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ validate value  public instance method """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
