#!/usr/bin/python3
""" class  defines a rectangle """


class Rectangle:
    """ define class Rectangle with private instance size """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        width : width of rectangle
        height : height of rectangle
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
        return self.width * self.height

    def perimeter(self):
        """ returns current rectangle area """
        if self.height == 0 or self.width == 0:
            return 0
        return (self.height + self.width) * 2

    def __str__(self):
        """ return representation rectangle in str-rectangle  """
        str_rectangle = ""
        if self.__height == 0 or self.__width == 0:
            return str_rectangle
        for i in range(self.height):
            for j in range(self.width):
                str_rectangle += str(self.print_symbol)
            if i < self.height - 1:
                str_rectangle += "\n"
        return str_rectangle

    def __repr__(self):
        """ return objet function representation of rectangle """
        return "Rectangle({:d}, {:d})".format(self.width, self.height)

    def __del__(self):
        """ print the message when an instance of rectangle is deleted """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
