#!/usr/bin/python3
"""Define a class MyList"""


class MyList(list):
    """a subclass of list"""

    def print_sorted(self):
        """prints the sorted list in ascending order"""
        print(sorted(self))
