#!/usr/bin/python3

"""
rectangle   class for the rectangle  
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        """assogming 

        Args:
            size (int): _description_
            x (int, optional): _description_. Defaults to 0.
            y (int, optional): _description_. Defaults to 0.
            id (_type_, optional): _description_. Defaults to None.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        else:
            if size <= 0:
                raise ValueError("size must be > 0")
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        if args:
            try:
                self.id = args[0]
                self.width = args[1]
                self.height = args[1]
                self.x = args[2]
                self.y = args[3]
            except IndexError:
                pass
        else:
            for key in kwargs.keys():
                try:
                    if key == "size":
                        self.__setattr__("width", kwargs[key])
                        self.__setattr__("height", kwargs[key])
                        continue
                    self.__setattr__(key, kwargs[key])
                except AttributeError:
                    pass

    def to_dictionary(self):
        """return dictinary of the user
        """
        return {
            'id': self.id,
            'x': self.x,
            'y': self.y,
            'size': self.width,
        }

    def __str__(self):
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
