#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    r = []
    for e in my_list:
        if e % 2 == 0:
            r.append(True)
        else:
            r.append(False)
    return r
