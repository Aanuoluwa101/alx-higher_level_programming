#!/usr/bin/python3
for _ in range(ord('a'), ord('z') + 1):
    if chr(_) == 'e' or chr(_) == 'q':
        continue
    else:
        print(chr(_), end="")
