#!/usr/bin/python3
"""Defines an object attribute lookup function"""


def lookup(obj):
    """Returns an object's available attributes

    Args:
        obj(any object): the object
    Returns:
        a list of the attributes of obj
    """
    return(dir(obj))
