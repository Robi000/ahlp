#!/usr/bin/python3

"""9-student
Contains class Student
"""


class Student:
    """Base class for subsequent tasks"""

    def __init__(self, first_name, last_name, age):
        """Initializes the attributes of this class"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs and type(attrs) is list:
            dicc = self.__dict__
            dic = {}
            for key in dicc:
                if key in attrs:
                    dic[key] = dicc[key]
            return dic

        """Retrieves the dictionary representation of Student"""
        return self.__dict__

    def reload_from_json(self, json):
        """Replaces all attributes of the Student instance
        Args:
            json (dict): JSON dict to get attributes and their values from
        """
        for i, j in zip(json.keys(), json.values()):
            setattr(self, i, j)
