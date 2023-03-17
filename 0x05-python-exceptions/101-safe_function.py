#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        result = fct(*args)
        return result
    except BaseException:
        print("Exception: {}".format(sys.exc_info()[0]), file=sys.stderr)
        return None
