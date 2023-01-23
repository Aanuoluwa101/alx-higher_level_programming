#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    i = 0
    while (x >= 1):
        try:
            print(my_list[i], end="")
            i += 1
            x -= 1
        except IndexError:
            break
    print("")
    return (i)
