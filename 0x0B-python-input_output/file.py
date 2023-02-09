#!/usr/bin/python3

with open("testfile.txt", "r+", encoding="utf-8") as f:
    print(f.tell())
    line = f.readline()
    f.seek(f.tell())
    f.write("\"C is fun!\"\n")
    """while line:
        if "o" in line:
            f.seek(f.tell())
            f.write("\"C is fun!\"\n")
            line = f.readline()
            line = f.readline()
        else:
            line = f.readline()"""
    f.seek(0, 0)
    print(f.read())
