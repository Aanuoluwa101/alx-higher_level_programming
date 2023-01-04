#!/usr/bin/python3
def letter(n):
    if n % 2 == 0:
        return n
    else:
        return (n - 32)


for n in range(ord('z'), ord('a') - 1, -1):
    print("{}".format(chr(letter(n))), end="")
