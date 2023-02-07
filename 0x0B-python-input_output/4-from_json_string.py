#!/usr/bin/python3
"""Dines a JSON string-to-python data structure function"""
import json


def from_json_string(my_str):
    """Returns a python object represented by a JSON string

    Args:
        my_str (str): JSON string
    Returns:
        an object (Python data structure)
    """
    return(json.loads(my_str))
