#!/usr/bin/python3
"""Module to find the max integer in a list
"""
import numpy

def lazy_matrix_mul(m_a, m_b):
    """Function to find and return the max integer in a list of integers
        If the list is empty, the function returns None
    """

    return numpy.matmul(m_a, m_b)

print(lazy_matrix_mul([[3, 4]], [[3, 4]]))
