#!/usr/bin/python3
def uppercase(str):
    i = 0
    for c in str:
        i += 1
        if (i == len(str)):
            re = "\n"
        else:
            re = ""
        if ord(c) >= ord("a") and ord(c) <= ord("z"):
            print("{}{}".format(chr(ord(c) - ord("a") + ord("A")), re), end="")
        else:
            print("{}{}".format(c, re), end="")
