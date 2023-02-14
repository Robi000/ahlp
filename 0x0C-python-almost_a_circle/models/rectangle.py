#!/usr/bin/python3

"""
rectangle   class for the rectangle  
"""
from models.base import Base


class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        """initial the class with data 

        Args:
            width (int): >0
            height (int): >0
            x (int, optional): >=0. Defaults to 0.
            y (int, optional): >=0. Defaults to 0.
            id (int, optional): anythig. Defaults to None.
        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        else:
            if width <= 0:
                raise ValueError("width must be > 0")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        else:
            if height <= 0:
                raise ValueError("height must be > 0")
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        else:
            if x < 0:
                raise ValueError("x must be >= 0")
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        else:
            if y < 0:
                raise ValueError("y must be >= 0")
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id=id)

    def area(self):
        """return area

        Returns:
            int: area 
        """
        return self.__width * self.__height

    def display(self):
        """display the rectangle using #
        """
        for x in range(self.__y):
            print()
        for x in range(self.__height):
            print(" "*self.__x, end="")
            print("#" * self.__width)

    def update(self, *args, **kwargs):
        if args:
            try:
                self.id = args[0]
                self.width = args[1]
                self.height = args[2]
                self.x = args[3]
                self.y = args[4]
            except IndexError:
                pass
        else:
            for key in kwargs.keys():
                self.__setattr__(key, kwargs[key])

    def __str__(self):
        """return string representation 

        Returns:
            string : ---
        """
        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - {self.__width}/{self.__height}"

    def to_dictionary(self):
        """return dictinary of the user
        """
        return {
            'id': self.id,
            'x': self.x,
            'y': self.y,
            'width': self.width,
            'height': self.height
        }

    @property
    def width(self):
        """return width

        Returns:
            int: width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """set width

        Args:
            value (int): width
        """
        width = value
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        else:
            if width <= 0:
                raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """return height

        Returns:
            int: return
        """
        return self.__height

    @height.setter
    def height(self, value):
        """set height 

        Args:
            value (int): return height 
        """
        height = value
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        else:
            if height <= 0:
                raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """return x

        Returns:
            int: x
        """
        return self.__x

    @x.setter
    def x(self, value):
        """set x

        Args:
            value (int): x
        """
        x = value
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        else:
            if x < 0:
                raise ValueError("x must be > 0")
        self.__x = value

    @property
    def y(self):
        """set y

        Returns:
            int: y value
        """
        return self.__y

    @y.setter
    def y(self, value):
        """set y 

        Args:
            value (int): y value
        """
        y = value
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        else:
            if y < 0:
                raise ValueError("y must be > 0")
        self.__y = value
