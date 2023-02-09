#!usr/bin/python3
"""Defines a function that checks the class of an object"""


if __name__ == "__main__":
    def is_same_class(obj, a_class):
        """Tells if an object is exactly an instance of a specified class

        Args:
            obj (any): the object
            a_class (type): the class against which the object is checked
        Returns:
            True if the object is exactly an instance of the specified class
            False if otherwise
        """
        return (type(obj) == a_class)
