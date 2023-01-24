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