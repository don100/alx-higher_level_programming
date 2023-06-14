#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    x = [[int(y**2) for y in x] for x in matrix]
    return x
