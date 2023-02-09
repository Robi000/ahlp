#!/usr/bin/python3

"""
base class for the base 
"""

class Base():

    """
    the base class 

    """
    __nb_objects = 0

    def __init__(self, id=None):
        """initialize 

        Args:
            id (int , optional): id of the obj. Defaults to None.
        """
        if id is not None:
            self.id = id
        else:

            Base.__nb_objects += 1
            self.id = self.__nb_objects


