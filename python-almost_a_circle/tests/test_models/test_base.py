#!/usr/bin/python3
"""
unittest for class Base
"""
import unittest
import json
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBaseClass(unittest.TestCase):
    """ tests Base """


    def test_init_with_id(self):
        b = Base(5)
        self.assertEqual(b.id, 5)

    def test_init_without_id(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)

    def test_to_json_value(self):
        sq = Square(10, 5, 5, 50)
        js_dict = sq.to_dictionary()
        js_str = Base.to_json_string([js_dict])
        self.assertEqual(
            json.loads(js_str), [{"id": 50, "y": 5, "size": 10, "x": 5}])

if __name__ == '__main__':
    unittest.main()
