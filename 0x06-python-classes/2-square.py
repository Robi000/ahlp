#!/usr/bin/python3

"""Square with size attribute, throws exceptions if size is not valid
    and with a public method that returns the area
    """

class Square ():
    """Square with size attribute, throws exceptions if size is not valid
    and with a public method that returns the area
    """
    
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