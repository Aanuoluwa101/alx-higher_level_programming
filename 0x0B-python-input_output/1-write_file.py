#!/usr/bin/python3
"""Defines a file-writing function"""


def write_file(filename="", text=""):
    """writes a string to a text file (UTF8)

    Args:
        filename (str): name of the file to be written to
        text (str): the string to be written
    Returns:
        The number of characters written
    """
    if type(filename) != str:
        raise TypeError("Filename must be a string")
    if filename == "":
        raise ValueError("Filename cannot be an empty string")
    if type(text) != str:
        raise ValueError("text must be a string")

    with open(filename, "w", encoding="utf-8") as f:
        chr_count = f.write(text)

    return chr_count
