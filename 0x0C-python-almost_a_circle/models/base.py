#!/usr/bin/python3

"""
base class for the base 
"""
import json


class Base():

    """
    the base class  created verry cool very very cool base

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

    @staticmethod
    def to_json_string(list_dictionaries):
        """to json string 

        Args:
            list_dictionaries (dic): dic

        Returns:
            str: json str
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def create(cls, **dictionary):
        """create instance from dictinary 

        Returns:
            obj : rectnagele or squre object
        """
        if cls.__name__ == "Rectangle":
            obj = cls(1, 1)
        else:
            obj = cls(1)

        obj.update(**dictionary)
        return obj

    @classmethod
    def save_to_file(cls, list_objs):
        """save obj to file 

        Args:
            list_objs (list ): object list 
        """
        name = cls.__name__+".json"
        list_dictionaries = []
        if list_objs != None:
            for obj in list_objs:
                list_dictionaries.append(obj.to_dictionary())
        # print(list_dictionaries)
        with open(name, "w") as f:
            f.write(Base.to_json_string(list_dictionaries))

    @staticmethod
    def from_json_string(json_string):
        """from json string to dic

        Args:
            json_string (string ): json string 

        Returns:
            dict : dict representation of the json string 
        """
        if json_string is None:
            return []

        else:
            return json.loads(json_string)

    @classmethod
    def load_from_file(cls):
        """create object from file 

        Returns:
            obj : created from file 
        """
        file_name = cls.__name__ + ".json"
        try:
            with open(file_name, "r") as f:
                dict = cls.from_json_string(f.read())
                lis_obj = []
                for x in dict:
                    lis_obj.append(cls.create(**x))
                return lis_obj
        except FileNotFoundError:
            return []
