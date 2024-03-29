#!/usr/bin/python3

if __name__ == "__main__":
    """Print the number of and list of arguments."""

    import sys

    count = len(sys.argv) - 1
    if count == 0:
        print("0 arguments.")
    elif count == 1:
        print("1 argument:\n{}: {}".format(count, sys.argv[1]))
    else:
        print("{} arguments:".format(count))
        for n in range(1, count):
            print("{}: {}".format(n, sys.argv[n]))
