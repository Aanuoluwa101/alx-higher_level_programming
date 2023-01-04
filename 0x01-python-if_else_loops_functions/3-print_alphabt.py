#!/usr/bin/python3
for n in range(ord('a'), ord('z') + 1):
    if chr(n) == 'e' or chr(n) == 'q':
        continue
    else:
        print("{}".format(chr(n)), end="")
