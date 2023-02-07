#!/usr/bin/python3
"""Defines a file-appending function"""


def append_write(filename="", text=""):
    """appends a string at the end of a text file (UTF8)

    Args:
        filename (str): name of the file to be appended to
        text (str): the string to be appended
    Returns:
        The number of characters added
    """
    if type(filename) != str:
        raise TypeError("Filename must be a string")
    if filename == "":
        raise ValueError("Filename cannot be an empty string")
    if type(text) != str:
        raise ValueError("text must be a string")

    with open(filename, "a", encoding="utf-8") as f:
        chr_count = f.write(text)

    return chr_count
