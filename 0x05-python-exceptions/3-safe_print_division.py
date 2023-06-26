#!/usr/bin/python3
def safe_print_division(a, b):
    d = None
    s = ""
    try:
        d = a / b
    except (TypeError, ZeroDivisionError, ValueError):
        return None
    finally:
        print("Inside result: {:d}".format(d))
    return d
