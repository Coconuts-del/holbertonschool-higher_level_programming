#!/usr/bin/python3
"""
    Creation of child class Rectangle of class BaseGeometry
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
        defines Rectangle child class of BaseGeometry
        wihout using getter an setter
        height and width are private
    """
    def __init__(self, width, height):
        """ call method integer_validator """
        self.integer_validator('width', width)
        self.integer_validator('height', height)
        self.__with = width
        self.__height = height
