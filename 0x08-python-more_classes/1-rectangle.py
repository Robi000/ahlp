#!/usr/bin/python3
# -*- coding: utf-8 -*-


class Rectangle:

    """ this is the class of the rectangle """

    def __init__(self, width=0, height=0):
        """we initalize all what we need here and do our job 
        """

        self.__width = width
        self.__height = height

    @property
    def width(self):
        """return  width 

        Returns:
            int: width of the rectangle 
        """

        return self.__width

    @width.setter
    def width(self, value):
        """initalize width with value


        Args:
            value (int): rectangle width 

        Raises:
            TypeError: if its not int 
            TypeError: if its < 0
        """

        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """return  width 

        Returns:
            int: width of the rectangle 
        """

        return self.__height

    @height.setter
    def height(self, value):
        """initalize width with value


        Args:
            value (int): rectangle width 

        Raises:
            TypeError: if its not int 
            TypeError: if its < 0
        """

        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value
