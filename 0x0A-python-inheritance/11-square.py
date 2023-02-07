#!/usr/bin/python3
"""Defines a class Square based on the Rectangle class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represents a square"""

    def __init__(self, size):
        """initializes a square

        Args:
            size (int): the size of the square
        """
        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """returns the area of the square"""
        return (self.__size ** 2)

    def __str__(self):
        """Returns a string representation of the square"""
        return "[Square] {}/{}".format(self.__size, self.__size)
