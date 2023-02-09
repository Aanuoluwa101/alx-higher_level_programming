#!usr/bin/python3
"""Define a class Rectangle"""


class Rectangle:
    """Represent a Rectangle"""

    def __init__(self, width=0, height=0):
        """Initialize a new rectangle

        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get the value of the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the value of the width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Get the value of the height"""
        return self.__height

    @width.setter
    def height(self, value):
        """Set the value of the height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
