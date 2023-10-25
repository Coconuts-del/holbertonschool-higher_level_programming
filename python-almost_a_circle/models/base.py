#!/usr/bin/python3
"""
    defines a class
"""
import json


class Base:
    """ create class named base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """ initialize a new Base """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ return JSON string representation of list_dictionaries """
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ write list_ objs in filename using json """
        if list_objs is None:
            list_objs = []
        list_dict = []
        filename = cls.__name__ + ".json"
        with open(filename, "w", encoding="utf-8") as file:
            """ create and convert list_dict to list of dictionaries """
            for i in list_objs:
                list_dict.append(i.to_dictionary())
            file.write(Base.to_json_string(list_dict))

    @staticmethod
    def from_json_string(json_string):
        """ return the list of the JSON string representation json_string """
        if json_string is None:
            return "[]"
        return json.loads(json_string)
