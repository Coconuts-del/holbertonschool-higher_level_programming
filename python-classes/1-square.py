#!/usr/bin/python3
""" defines a class """


class Square:
    """ define class Square with private instance size """
    def __init__(self, size):
        """ size : no verification on type & value """
        self.__size = size
