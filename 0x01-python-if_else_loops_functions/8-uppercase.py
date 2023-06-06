#!/usr/bin/python3
def uppercase(str):
    tx = ""
    for c in str:
        tx = c
        if ord(c) >= ord("a") and ord(c) <= ord("z"):
            tx = chr(ord(c) - ord("a") + ord("A"))
        print("{}".format(tx), end="")
    print("")
