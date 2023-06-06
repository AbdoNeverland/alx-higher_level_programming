#!/usr/bin/python3
def uppercase(str):
    tx = ""
    for c in str:
        tx = chr(ord(c) - ord("a") + ord("A"))
        if ord(c) >= ord("a") and ord(c) <= ord("z"):
            print("{}".format(tx), end="")
    print("")
uppercase("best")
uppercase("Best School 98 Battery street")
