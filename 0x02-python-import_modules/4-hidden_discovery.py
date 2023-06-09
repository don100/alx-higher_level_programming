#!/usr/bin/python3
if __name__ != "__main__":
    exit()
import hidden_4
for a in dir(hidden_4):
    if a[:2] == "__":
        continue
    else:
        print(a)
