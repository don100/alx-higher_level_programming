#!/usr/bin/python3
if __name__ != "__main__":
    exit()
def square_matrix_simple(matrix=[]):
    return [[int(y**2) for y in x] for x in matrix]
