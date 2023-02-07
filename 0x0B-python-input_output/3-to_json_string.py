#!/usr/bin/python3
"""Defines a function that creates a JSON representation"""
import json


def to_json_string(my_obj):
    """returns the JSON representation of an object (string)

    Args:
        obj (str): the string to be represented in json format
    Returns:
        a JSON representation of obj
    """
    return(json.dumps(my_obj))
