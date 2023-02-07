#!/usr/bin/python3
"""Defines a function that reads a JSON file"""
import json


def load_from_json_file(filename):
    """Creates an object from a JSON file

    Args:
        filename (str): name of the JSON file to be read
    """
    if type(filename) != str:
        raise TypeError("Filename must be a string")
    if filename == "":
        raise ValueError("Filename cannot be an empty string")

    with open(filename, encoding="utf-8") as f:
        return(json.load(f))
