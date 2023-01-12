#!/usr/bin/python3
def best_score(a_dictionary):
    """Returns a key with the biggest integer value."""
    if not isinstance(a_dictionary, dict) or len(a_dictionary) == 0:
        return None

    ret = list(a_dictionary.keys())[0]
    biggest = a_dictionary[ret]
    for i, j in a_dictionary.items():
        if j > biggest:
            biggest = j
            ret = i
    return ret
