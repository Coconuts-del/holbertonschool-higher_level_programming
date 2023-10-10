#!/usr/bin/python3
""" defines a class """


class Square:
    """ define class Square with private instance size """
    def __init__(self, size=0):
        """ size : verification on type & value """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """ returns current square area """
        return self.__size ** 2
