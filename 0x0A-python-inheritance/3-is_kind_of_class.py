#!usr/bin/python3

def is_kind_of_class(obj, a_class):
    """Tells if an object is exactly an instance of a class or its subclass

    Args:
        obj (any): the object
        a_class (type): the class against which the object is checked
    Returns:
        True if the object is an instance of the specified class
        or one of its subclasses or False if otherwise
    """
    return isinstance(obj, a_class)
