#!usr/bin/python3
"""Defines a function that checks inheritance"""


if __name__ == "__main__":
    def inherits_from(obj, a_class):
        """Tells if the object is an instance of a class that
           inherited from the specified class

        Args:
            obj (any): the object
            a_class (type): the class against which the object is checked
        Returns:
            True if the object is an instance of a class that inherited
            (directly or indirectly) from the specified class or False if otherwise
        """
        if not issubclass(obj.__class__, a_class) or type(obj) == a_class:
            return False
        return True
