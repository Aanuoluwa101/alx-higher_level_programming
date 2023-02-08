#!/usr/bin/python3
load_from_json = __import__("6-load_from_json_file").load_from_json_file

my_list = load_from_json("list.json")
print(my_list)
