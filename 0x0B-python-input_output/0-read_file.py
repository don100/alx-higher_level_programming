#!/usr/bin/python3
''' 0-read_file.py '''


def read_file(filename=""):
    '''  Read file '''
    import sys
    with open(filename, encoding="utf-8") as f:
        read_data = f.read()
    sys.stdout.write(read_data)
