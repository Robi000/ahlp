#!/usr/bin/python3


"""Square with size attribute, throws exceptions if size is not valid
    and with a public method that returns the area
    """


class Square ():
    """Square with size attribute, throws exceptions if size is not valid
    and with a public method that returns the area
    """
    def __init__(self, size=0, position=(0, 0)):
        """initallize the class

        Args:
            size (int): size of the square
        """
        if not isinstance(size , int):
            raise TypeError ("size must be an integer")
        else:
            if size < 0:
                raise ValueError ("size must be >= 0")
        
        if not isinstance(position , tuple):
            raise TypeError ("position must be a tuple of 2 positive integers")
        else:
            if not isinstance(position[0], int) or not isinstance(position[1], int):
                raise TypeError ("position must be a tuple of 2 positive integers")
        self.__size = size
        self.__position = position
    

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
    

    def my_print(self):
        """this will print squre hashtag 

        print squrer hashtag
        """
        for i in range(self.__position[1]):
            print("")
        for i in range(self.__size):
            print(" " * self.__position[0], end= "")
            print("#" * self.__size)

    @property
    def position(self):
        """size getter

        Returns:
            int : nothing 
        """
        return self.__position
    
    @position.setter
    def position (self, value):
        position = value
        """set the value of the size

        Args:
            value (int): size of the squere

        Raises:
            TypeError: raise when the size is not int
            ValueError: raise whten the size is < 0
        """
        if not isinstance(position , tuple):
            raise TypeError ("position must be a tuple of 2 positive integers")
        else:
            if not isinstance(position[0], int) or not isinstance(position[1], int):
                raise TypeError ("position must be a tuple of 2 positive integers")

        self.__position = position
