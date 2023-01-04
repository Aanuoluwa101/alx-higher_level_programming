#!/usr/bin/python3
for _ in range(ord('z'), ord('a') - 1, -1):
    if _ % 2 == 0:
        print(f"{chr(_)}", end="")
    else:
        print(f"{chr(_ - 32)}", end="")
