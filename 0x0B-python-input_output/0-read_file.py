#!/usr/bin/python3
"""Defines a file-reading function"""


def read_file(filename=""):
    """reads a text file (UTF8) and prints it to stdout

    Args:
        filename (str): name of the file to be read
    """
    if type(filename) != str:
        raise TypeError("Filename must be a string")
    if filename == "":
        raise ValueError("Filename cannot be an empty string")

    with open(filename, encoding="utf-8") as f:
        for line in f:
            print(line, end="")
