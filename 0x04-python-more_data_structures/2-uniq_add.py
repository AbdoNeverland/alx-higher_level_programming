#!/usr/bin/python3
def uniq_add(my_list=[]):
    n = []
    somme = 0
    for e in my_list:
        if e not in n:
            somme += e
            n.append(e)
    return somme
