#!/usr/bin/python3
def isupper(c):
    if ord(c) >= 65 and ord(c) <= 90:
        return True
    else:
        return False


def uppercase(str):
    for i in range(len(str)):
        if islower(str[i]):
            print(chr(ord(str[i]) - 32), end="")
        else:
            print(str[i], end="")
