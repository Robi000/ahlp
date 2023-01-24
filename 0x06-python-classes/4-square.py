#!/usr/bin/python3

class Square ():
    
    def __init__(self, size=0):
        """initallize the class

        Args:
            size (int): size of the square
        """
        if not isinstance(size , int):
            raise TypeError ("size must be an integer")
        else:
            if size < 0:
                raise ValueError ("size must be >= 0")
        self.__size = size
    

    def area(self):
        """return the area of the square 

        Returns:
            int : area
        """
        return self.__size **2

    @property
    def size(self):
        """size getter

        Returns:
            int : nothing 
        """
        return self.__size
    
    @size.setter
    def size (self, value):
        """set the value of the size

        Args:
            value (int): size of the squere

        Raises:
            TypeError: raise when the size is not int
            ValueError: raise whten the size is < 0
        """
        if not isinstance(value , int):
            raise TypeError ("size must be an integer")
        else:
            if value < 0:
                raise ValueError ("size must be >= 0")
        self.__size = value