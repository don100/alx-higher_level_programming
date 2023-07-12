#!/usr/bin/python3
''' module '''


def pascal_triangle(n):
    ''' pascal_triangle '''
    pascal = []
    items = []
    if n <= 0:
        return pascal
    for i in range(n):
        for j in range(i):
            items.append(pascal[i-1][j] + (pascal[i-1][j-1] if j-1 >= 0 else 0))
        items.append(1)
        pascal.append(items)
        items = []
    return pascal
