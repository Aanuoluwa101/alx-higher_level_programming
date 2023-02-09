#!/usr/bin/python3
"""Defines a function that inserts strings into a file"""


def append_after(filename="", search_string="", new_string=""):
    	""" inserts a line of text to a file,
            after each line containing a specific string

        Args:
            filename (str): name of the file
            search_string (str): the string to be searched for
            new_string (str): the string to be inserted
        """
        if type(filename) not str:
            raise TypeError("filename must be a string")
        if not filename:
            raise("filename cannot be empty")
        with open(filename, "r+", encoding="utf-8") as f:
            lines = f.readlines()
            if search_string in lines[-1]:
                lines.append(new_string)
            else:
                for index range(len(lines)):
                    if search_string in lines[index]:
                        lines.insert[index, new_string]
                    else:
                        continue
        f.seek(0)
        f.writelines(lines)
