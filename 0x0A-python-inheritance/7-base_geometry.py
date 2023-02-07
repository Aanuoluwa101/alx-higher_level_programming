#!/usr/bin/python3
"""Define a class BaseGeometry"""


class BaseGeometry:
    """Represent base geometry"""

    def area(self):
        """raises an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates value as an integer

        Args:
            name (str): the name of the parameter
            value (str): the value of the parameter
        Raises:
            TypeError: if the value is not an integer
            ValueError: if the value is less than or equal to 0
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
