#!/usr/bin/python3
""" defines a class """


class Square:
    """ define class Square with private instance size """
    def __init__(self, size=0):
        """ size : square size  """
        self.size = size

    @property
    def size(self):
        """ retrieve size """
        return self.__size

    @size.setter
    def size(self, value):
        """ size : set and validate size (type & value) """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ returns current square area """
        return self.__size ** 2

    def my_print(self):
        """ print square with hash chars """
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end="")
            print()
        if self.__size is 0:
            print()
