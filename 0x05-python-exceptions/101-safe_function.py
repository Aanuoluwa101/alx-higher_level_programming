#!/usr/bin/python3

def safe_function(fct, *args):
    try:
        result = fct(*args)
        return result
    except Exception as ex:
        print("Exception: {}".format(ex), file=sys.stderr)
        return None
