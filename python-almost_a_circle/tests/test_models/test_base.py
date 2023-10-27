#!/usr/bin/python3
"""
unittest for class Base
"""
import unittest
from models.base import Base


class TestBaseClass(unittest.TestCase):
    """ tests Base """
    def test_id(self):
        self.assertEqual(Base(5).id, 5)
        self.assertEqual(Base().id, 1)
        self.assertEqual(Base().id, 2)
        self.assertEqual(Base(180).id, 180)
    
    def test_to_json_string_none(self):
        self.assertEqual(Base.to_json_string(None), '[]')

    def test_to_json_string_empty(self):
        self.assertEqual(Base.to_json_string([]), '[]')

    def test_to_json_string_exists(self):
        self.assertEqual(Base.to_json_string([{'id': 80}]), '[{"id": 80}]')

    def test_from_json_string_none(self):
        self.assertEqual(Base.from_json_string(None), [])

    def test_from_json_string_empty(self):
        self.assertEqual(Base.from_json_string("[]"), [])

    def test_from_json_string_exists(self):
        self.assertEqual(Base.from_json_string('[{ "id": 52}]'), [{'id': 52}])
        
if __name__ == '__main__':
    unittest.main()
