#!/usr/bin/python3
""" defines a class """


class Square:
    """ define class Square with private instance size """
    def __init__(self, size=0, position=(0, 0)):
        """
        size : side of square
        position : tuple of 2 positive integers
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """ retrieve position of the square """
        return self.__position

    @position.setter
    def position(self, value):
        """  position : set and validate tuple of 2 positive integers """
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """ returns current square area """
        return self.__size ** 2

    def my_print(self):
        """ print square with hash chars at position """
        if self.__size == 0:
            print()
        else:
            for v_pos in range(self.__position[1]):
                print()
            for i in range(self.__size):
                for h_pos in range(self.__position[0]):
                    print(" ", end="")
                for j in range(self.__size):
                    print("#", end="")
                print()
