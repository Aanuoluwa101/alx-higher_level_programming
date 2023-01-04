#!/usr/bin/python3
def uppercase(str):
    str1 = ""
    for char in str:
        if ord(char) >= 97 and ord(char) <= 122:
            str1 += chr(ord(char) - 32)
        else:
            str1 += char
    print("{}".format(str1))
