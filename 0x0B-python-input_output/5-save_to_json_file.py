#!/usr/bin/python3
"""Defines a function that saves an object in JSON format"""
import json


def save_to_json_file(my_obj, filename):
    """writes an Object to a text file, using a JSON representation

    Args:
        filename (str): name of the file to be written to
        my_obj (any): the object
    """
    if type(filename) != str:
        raise TypeError("Filename must be a string")
    if filename == "":
        raise ValueError("Filename cannot be an empty string")

    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
