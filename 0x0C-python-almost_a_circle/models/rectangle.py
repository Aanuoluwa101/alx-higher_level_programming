#!/usr/bin/python3
"""Defines a Rectangle based on Base"""

class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a new Rectangle.
        Args:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
            x (int): The x coordinate of the new Rectangle.
            y (int): The y coordinate of the new Rectangle.
            id (int): The identity of the new Rectangle.
        Raises:
            TypeError: If either of width or height is not an int.
            ValueError: If either of width or height <= 0.
            TypeError: If either of x or y is not an int.
            ValueError: If either of x or y < 0.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)
        
    @property
    def width(self):
        """Get the width"""
        return self.__width
        
    @width.setter
    def width(self, width):
        """Set the width"""
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width
        
    @property
    def height(self):
        """Get the height"""
        return self.__height
        
    @height.setter
    def height(self, height):
        """Set the height"""
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height
            
    @property
    def x(self):
        """Get x"""
        return self.__x
        
    @x.setter
    def x(self, x):
        """Set x"""
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x
            
    @property
    def y(self):
        """Get y"""
        return self.__y
        
    @y.setter
    def y(self, y):
        """Set y"""
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y
        
    def area(self):
        """Returns the area of rectangle"""
        return self.__width * self.__height
            
    def __str__(self):
        """Returns a string representation of the rectangle"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x, self.__y, self.__width, self.__height)
        
    def display(self):
        """print in stdout the Rectangle instance with the character # by taking care of x and y"""
        for i in range(self.__y):
            print("\n")
    
        for i in range(self.__height):
            print(" " * self.__x , end="")
            for j in range(self.__width):
                print("#", end="")
            print("")
        
    def update(self, *args, **kwargs):
        """Assigns a key/value argument to each attribute
            
        Args:
            *args (list): list of arguments for the attributes to be updated in the order of
            id, width, height, x and y
            **kwargs (dictionary): dictionary of attribute/value
        """
        if args and args is not []:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y, self.id)
                    else:
                        self.id = arg
                elif a == 1:
                    self.width = arg
                elif a == 2:
                    self.height = arg
                elif a == 3:
                    self.x = arg
                elif a == 4:
                    self.y = arg
                a += 1
                
        elif kwargs and kwargs is not {}:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.width, self.height, self.x, self.y, self.id)
                    else:
                        self.id = v
                elif k == "width":
                    self.width = v
                elif k == "height":
                    self.height = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v
                    
    def to_dictionary(self):
        """Returns a dictionary representation of the rectangle"""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }
