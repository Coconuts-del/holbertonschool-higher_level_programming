#!/usr/bin/python3
""" class  defines a rectangle """


class Rectangle:
    """ define class Rectangle with private instance size """
    def __init__(self, width=0, height=0):
        """
        width : width of rectangle
        height : height of rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ retrieve width """
        return self.__width

    @width.setter
    def width(self, value):
        """ width : set and validate width (type & value) """
        if not isinstance(value, int):
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
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ returns current rectangle area """
        return self.__width * self.__height

    def perimeter(self):
        """ returns current rectangle area """
        if self.__height == 0 or self.__width == 0:
            return 0
        return (self.__height + self.__width) * 2

    def __str__(self):
        """ return representation rectangle in str-rectangle  """
        char = "#"
        str_rectangle = ""
        if self.__height == 0 or self.__width == 0:
            return str_rectangle
        for i in range(self.__height):
            for j in range(self.__width):
                str_rectangle += char
            if i < self.__height - 1:
                str_rectangle += "\n"
        return str_rectangle
