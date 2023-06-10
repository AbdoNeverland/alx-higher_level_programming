#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        if row:
            for i, col in enumerate(row):
                print("{:d}{}".format(col, " " if i < len(row) - 1 else "\n"),
                      end="")
