#!/usr/bin/python3
"""Defines a JSON serialization function"""


def class_to_json(obj):
    """Returns the dictionary description for JSON serialization of an object

    Args:
        obj (any): the object
    Returns:
        returns the dictionary description with simple data structure
        (list, dictionary, string, integer and boolean)
        for JSON serialization of an object
    """
    return obj.__dict__
