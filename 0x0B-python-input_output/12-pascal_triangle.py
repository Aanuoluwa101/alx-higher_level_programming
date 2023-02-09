#!/usr/bin/python3
"""Defines a function that wrtes a Pascal's triangle"""


def pascal_triangle(n):
    """Returns a list of lists of integers representing the Pascal’s triangle of n

    Args:
        n (int): height of the triangle
    Returns:
        a list of lists of integers representing the Pascal’s triangle of n
    """
    if n <= 0:
        return []

    pascal = [[] for i in range(n)]
    for i in range(n):
        if i == 0:
            pascal[i].append(1)
        else:
            former = pascal[i - 1]
            current = pascal[i]
	    new = [former[i] + former[i + 1]
                for i in range(len(former)) if i != len(former) - 1]
            current.append(1)
            current.extend(new)
            current.append(1)
    return pascal
