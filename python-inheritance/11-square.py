#!/usr/bin/python3
"""
    Creation of child class Square  of class Rectangle
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
        defines Square child class of Rectangle
        wihout using getter an setter
        size is private
    """
    def __init__(self, size):
        """ call method integer_validator """
        self.integer_validator('size', size)
        self.__size = size

    def __str__(self):
        """ print a string containing 'Square' size  and  size """
        return "[Square] {}/{}".format(self.__size, self.__size)

    def area(self):
        """ return  the area of the square """
        return self.__size * self.__size
