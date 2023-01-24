#!/usr/bin/python3

"""Square with size attribute, throws exceptions if size is not valid
    and with a public method that returns the area
    """

class Square ():
    """Square with size attribute, throws exceptions if size is not valid
    and with a public method that returns the area
    """
    
    def __init__(self, size):
        """initallize the class

        Args:
            size (int): size of the square
        """
        self.__size = size