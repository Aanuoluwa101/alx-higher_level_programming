#!/usr/bin/python3
import sys
import os
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"
if not os.path.exists(filename):
    save_to_json_file([], filename)

arg_list = load_from_json_file(filename)
for i in range(1, len(sys.argv)):
    arg_list.append(sys.argv[i])

save_to_json_file(arg_list, filename)
