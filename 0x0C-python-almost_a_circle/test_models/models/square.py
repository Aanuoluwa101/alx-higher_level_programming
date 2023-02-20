#/usr/bin/python3
"""Defines a class Square based on the Rectangle class"""


class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        """Initializes a square
        
        Args:
            size (int): the size (width and height) of the square
        """
        super().__init__(size, size, x, y, id)
        
    def __str__(self):
        """Returns a string representation of the square"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.size)
        
    @property
    def size(self):
        """Get size"""
        return self.width
    
    @size.setter
    def size(self, value):
        """Set size"""
        self.width = value
        self.height = value
        
    def update(self, *args, **kwargs):
        """Update the Square.
        Args:
            *args (ints): New attribute values.
                - 1st argument represents id attribute
                - 2nd argument represents size attribute
                - 3rd argument represents x attribute
                - 4th argument represents y attribute
            **kwargs (dict): New key/value pairs of attributes.
        """
        if args and args is not []:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.size = arg
                elif a == 2:
                    self.x = arg
                elif a == 3:
                    self.y = arg
                a += 1

        elif kwargs and kwargs is not []:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = v
                elif k == "size":
                    self.size = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v
        
    def to_dictionary(self):
        """Returns a dictionary representation of the square"""
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
        }