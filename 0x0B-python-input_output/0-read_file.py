#!/usr/bin/python3
''' 0-read_file.py '''
import sys


def read_file(filename=""):
    '''  Read file '''
    with open(filename, encoding="utf-8") as f:
        read_data = f.read()
    sys.stdout.write(read_data)
