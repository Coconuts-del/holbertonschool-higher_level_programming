#!/usr/bin/python3
""" define a square class """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ class named Square """

    def __init__(self, size, x=0, y=0, id=None):
        """ init a new Square """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ overriding __str__ method to return
            [Square] (<id>) <x>/<y> - <size> """
        x = str(self.x)
        y = str(self.y)
        return "[Square] ({}) {}/{} - {}".format(self.id, x, y, self.width)
