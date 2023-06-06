#!/usr/bin/python3
for i in range(97, 123, 1):
    if i != 113 and i != 101:
        print("{asc}".format(asc=chr(i)), end="")
