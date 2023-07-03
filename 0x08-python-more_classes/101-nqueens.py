#!/usr/bin/python3
import sys

if len(sys.argv) != 2
    print("Usage: nqueens N")
    exit(1)
if type(N) != int:
    print("N must be a number")
    exit(1)
if N < 4:
    print("N must be at least 4")
    exit(1)

N = sys.argv[1]
a = 0
queen = []
for i in range(N):
    for j in range(N):
        if i == j or i+j == N-1:
            continue
        queen.append([i, j])
        a+=1
        if a%N == 0:
            print(str(queen))
            queen = []
