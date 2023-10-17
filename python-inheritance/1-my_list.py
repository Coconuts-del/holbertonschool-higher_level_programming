#!/usr/bin/python3
""" Write a class MyList that inherits from list """


class MyList(list):
    """ MyList class """

    def print_sorted(self):
        """ printed sorted list """
        print(sorted(self))
