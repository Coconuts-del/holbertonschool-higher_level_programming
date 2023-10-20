#!/usr/bin/python3
"""
   Create a python object from a JSON file
"""
import json


def load_from_json_file(filename):
    """return an  object python  from JSON file """
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)
