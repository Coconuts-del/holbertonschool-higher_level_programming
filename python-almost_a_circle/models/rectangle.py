#!/usr/bin/python3
""" define a rectangle class """
from models.base import Base


class Rectangle(Base):
    """ class named Rectangle """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ init a new Rectangle """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """ retrieve width """
        return self.__width

    @width.setter
    def width(self, value):
        """ width : set and validate width (type & value) """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ retrieve height """
        return self.__height

    @height.setter
    def height(self, value):
        """ height : set and validate height (type & value) """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def x(self):
        """ retrieve x"""
        return self.__x

    @x.setter
    def x(self, value):
        """  set and validate x (type & value) """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ retrieve y """
        return self.__y

    @y.setter
    def y(self, value):
        """ set and validate y (type & value) """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
