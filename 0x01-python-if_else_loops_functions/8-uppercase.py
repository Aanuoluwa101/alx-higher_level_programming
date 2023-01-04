#!/usr/bin/python3
def islower(c):
    if ord(c) >= 97 and ord(c) <= 122:
        return True
    else:
        return False


def uppercase(str):
    str1 = ""
    for i in range(len(str)):
        if islower(str[i]):
            str1 += chr(ord(str[i]) - 32)
        else:
            str1 += str[i]
    print(f"{str1}")
