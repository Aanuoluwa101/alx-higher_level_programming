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

    def to_json(self):
        """retrieves a dictionary representation of the student"""
        return self.__dict__
