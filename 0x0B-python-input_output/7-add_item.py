#!/usr/bin/python3
""" module """
import sys


save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file
d = sys.argv
try:
    o = load_from_json_file("add_item.json")
except Exception as e:
    o = []
o.extend(d)
save_to_json_file(o, "add_item.json")
