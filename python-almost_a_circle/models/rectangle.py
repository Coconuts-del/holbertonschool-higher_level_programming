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
        if value <= 0:
            raise ValueError("width must be > 0")
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
        if value <= 0:
            raise ValueError("height must be > 0")
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

    def area(self):
        """ return  the area of the rectangle """
        return self.__width * self.__height

    def display(self):
        """ print stdout rectangle  with character # """
        """ print at the ordered """
        print("{}".format("\n" * self.__y), end="")
        for i in range(self.__height):
            """ print at the abscissa """
            print("{}".format(" " * self.__x), end="")
            for j in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """ overriding __str__ method to return
            [Rectangle] (<id>) <x>/<y> - <width>/<height> """
        return "[Rectangle] ({}) {}/{} - {}/{}".\
            format(self.id, self.__x, self.y, self.width, self.height)

    def update(self, *args):
        """ assign arguments to the 6 attributes """
        elem = ["id", "width", "height", "x", "y"]
        for i in range(len(args)):
            setattr(self, elem[i], args[i])
