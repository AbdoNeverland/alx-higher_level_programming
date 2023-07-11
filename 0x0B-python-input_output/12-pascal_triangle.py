#!/usr/bin/python3
""" module """


def pascal_triangle(n):
    """ fonction """
    d = []
    last = []
    for i in range(n):
        z = []
        for j in range(i + 1):
            if j != 0 and len(last) > j:
                z.append(last[j] + last[j - 1])
            else:
                z.append(1)
        last = z
        d.append(z)
    return d
