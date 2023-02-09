#!/usr/bin/python3
"""Defines a Student class"""


class Student:
    def __init__(self, first_name, last_name, age):
        """Initialize a student"""
        if type(first_name) != str or type(last_name) != str:
            raise TypeError("first and last name must be strings")
        if type(age) != int:
            raise TypeError("age must be an integer")
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of the student
            based on attrs
        """
        if attrs is not None and all(isinstance(obj, str) for obj in attrs):
            return {key: self.__dict__[key]
                    for key in attrs if key in self.__dict__}
        return self.__dict__

    def reload_from_json(self, json):
        """Replaces all attributes of the Student instance"""
        for attr in json:
            self.__dict__[attr] = json[attr]
