#!/usr/bin/python3
def roman_to_int(roman_string):
    data = {"I":1,"V":5,"X":10,"L":50,"C":100,
            "D":500,"M":1000}
    nl = list(map(lambda x: data[x], list(roman_number)))
    sum = i = 0
    while i < len(nl):
        if i != len(nl) - 1 and nl[i] < nl[i + 1]:
            sum += nl[i + 1] - nl[i]
            i += 1
        else:
            sum += nl[i]
        i += 1
    return sum
