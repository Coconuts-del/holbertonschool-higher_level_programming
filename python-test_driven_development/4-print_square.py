#!/usr/bin/python3
"""
  Print a square with the character #
  size  must be a integer > 0
  otherrwise raise typeerror exception
"""


def print_square(size):
    """ validation size """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    """ print square """
    for i in range(size):
        print("#" * size, end="")
        print()
