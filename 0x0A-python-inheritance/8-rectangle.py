#!/usr/bin/python3
"""Defines a class Rectangle based on the BaseGeometry class"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represents a rectangle"""

    def __init__(self, width, height):
        """initializes a rectangle

        Args:
            width (int): the width of the new rectangle
            height (int): the height of the new rectangle
        """
        super().__init__()

        super().integer_validator("width", width)
        self.__width = width

        super().integer_validator("height", height)
        self.__height = height
