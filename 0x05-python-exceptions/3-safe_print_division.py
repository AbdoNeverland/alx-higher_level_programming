#!/usr/bin/python3
def safe_print_division(a, b):
    d = None
    s = ""
    try:
        d = a / b
        s = "Inside result: {:d}".format(d)
    except (TypeError, ZeroDivisionError, ValueError):
        return d
    finally:
        print(s)
