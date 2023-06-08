#!/usr/bin/python3
import hidden_4

if __name__ == "__main__":
    sum = 0
    for arg in dir(hidden_4):
        if not arg.startswith("__"):
            print(arg)
