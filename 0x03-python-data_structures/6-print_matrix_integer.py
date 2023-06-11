#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[0])):
            str = " " if j < len(matrix[0]) - 1 else ""
            print("{:d}{}".format(matrix[i][j], str), end="")
        print()
