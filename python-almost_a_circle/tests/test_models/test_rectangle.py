#!/usr/bin/python3
"""
unittest for class Rectangle
"""
import unittest
from models.rectangle import Rectangle
from models.base import Base


class TestRectangleClass(unittest.TestCase):
    """ tests Rectangle """
    def test_rectangle_creation_1 (self):
        rect = Rectangle(10, 5)
        self.assertEqual(rect.width, 10)
        self.assertEqual(rect.height, 5)

    def test_rectangle_creation_2(self):
        rect = Rectangle(10, 5, 3)
        self.assertEqual(rect.width, 10)
        self.assertEqual(rect.height, 5)
        self.assertEqual(rect.x, 3)

    def test_rectangle_creation_3(self):
        rect = Rectangle(10, 5, 3, 4)
        self.assertEqual(rect.width, 10)
        self.assertEqual(rect.height, 5)
        self.assertEqual(rect.x, 3)
        self.assertEqual(rect.y, 4)

    def test_type(self):
        self.assertRaises(TypeError, Rectangle, "10", 10)      
        self.assertRaises(TypeError, Rectangle, width = "10")      
        self.assertRaises(TypeError, Rectangle, 10, height = "ig5")      
        self.assertRaises(TypeError, Rectangle, 10, x = 2.5)      
        self.assertRaises(TypeError, Rectangle, 10, y = None)      

    def test_value(self):
        self.assertRaises(ValueError, Rectangle, -10, 5)      
        self.assertRaises(ValueError, Rectangle, 0, 5)      
        self.assertRaises(ValueError, Rectangle, 5, -10)      
        self.assertRaises(ValueError, Rectangle, 5, 0)      
        self.assertRaises(ValueError, Rectangle, 10, 5, -3, 4)      
        self.assertRaises(ValueError, Rectangle, 10, 5, 3, -4)      
    
    def test_area(self):
        rect = Rectangle(10, 5)
        self.assertEqual(rect.area(), 50)

if __name__ == '__main__':
    unittest.main()
