#!/usr/bin/python3
def safe_print_division(a, b):
    d = None
    try:
        d = a / b
    except (TypeError, ZeroDivisionError, ValueError):
        d = None
    finally:
        print("Inside result: {}".format(d))
    return d
