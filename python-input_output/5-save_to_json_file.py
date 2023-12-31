#!/usr/bin/python3
"""
   writes an Object to a text file, using a JSON representation
"""
import json


def save_to_json_file(my_obj, filename):
    """write my _obj in filename using json"""
    with open(filename, "w", encoding="utf-8") as file:
        file.write(json.dumps(my_obj))
