#!usr/bin/python3
"""Define a class Rectangle"""


class Rectangle:
    """Represent a Rectangle"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize a new rectangle

        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle
        """
        self.width = width
        self.height = height
        number_of_instances += 1

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

    def area(self):
        """Returns the area of the rectangle"""
        return self.__height * self.__width

    def perimeter(self):
        """Returns the perimeter of the rectangle"""
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return 2 * (self.__height + self.__width)

    def __str__(self):
        """Return a string representation of the rectangle
        using the print symbol"""
        rect = []
        if self.__height == 0 or self.__width == 0:
            return("")
        for i in range(0, self.__height):
            [rect.append(print_symbol) for j in range(self.__width)]
            if i != self.__height - 1:
                rect.append("\n")
        return("".join(rect))

    def __repr__(self):
        """Return a string representation of the rectangle"""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Rectangle Destructor method"""
        number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Returns the biggest rectangle based on the area"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        else:
            area_1 = rect_1.area()
            area_2 = rect_2.area()
            if area_1 >= area_2:
                return rect_1
            else:
                return rect_2

    @classmethod
    def square(cls, size=0):
        return cls(size, size)
