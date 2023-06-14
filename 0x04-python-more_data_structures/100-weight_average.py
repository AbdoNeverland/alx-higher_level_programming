#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    dv = sm = 0
    for e in my_list:
        dv += e[1]
        sm += e[0] * e[1]
    if not dv:
        return 0
    return sm / dv
