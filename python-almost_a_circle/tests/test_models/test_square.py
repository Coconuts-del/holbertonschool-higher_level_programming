#!/usr/bin/python3
"""
unittest for class Square
"""
import unittest
from models.square import Square
from models.base import Base


class TestSquare(unittest.TestCase):
    """ tests Square """
    def test_square_creation_1 (self):
        sq = Square(10)
        self.assertEqual(sq.size, 10)

    def test_square_creation_2(self):
        sq = Square(10, 3)
        self.assertEqual(sq.size, 10)
        self.assertEqual(sq.x, 3)

    def test_square_creation_3(self):
        sq = Square(10, 3, 4)
        self.assertEqual(sq.size, 10)
        self.assertEqual(sq.x, 3)
        self.assertEqual(sq.y, 4)

    def test_square_creation_4(self):
        sq = Square(10, 3, 4, 50)
        self.assertEqual(sq.size, 10)
        self.assertEqual(sq.x, 3)
        self.assertEqual(sq.y, 4)
        self.assertEqual(sq.id, 50)

if __name__ == '__main__':
    unittest.main()
