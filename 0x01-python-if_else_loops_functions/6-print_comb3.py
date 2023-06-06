#!/usr/bin/python3
for i in range(0, 8, 1):
    for j in range(i, 10, 1):
        if i != j:
            print("{}{}, ".format(i, j), end="")
print("{}{}".format((i + 1), j))
