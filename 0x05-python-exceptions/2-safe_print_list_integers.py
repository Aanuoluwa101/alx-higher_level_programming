#!usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    count = 0
    for num in range(x):
        try:
            print("{}".format(my_list[num]), end="")
            count += 1
        except (ValueError, IndexError):
            continue
    print("")
    return count
