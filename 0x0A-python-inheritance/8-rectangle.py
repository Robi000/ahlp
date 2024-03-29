#!/usr/bin/python3

"""7-base_geometry
Contains class BaseGeometry
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Empty class with just one method
    """
    def __init__(self, width, height):
        """Initialize the object's values"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
