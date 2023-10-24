#!/usr/bin/python3
"""
unittest for class Base
"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """ test if id is correct """
    def test_init(self):
        b = Base()
        self.assertEqual(b.id, 1)

        b = Base(15)
        self.assertEqual(b.id, 15)


if __name__ == '__main__':
    unittest.main()
