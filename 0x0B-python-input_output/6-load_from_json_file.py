#!/usr/bin/python3
''' module python3 '''
import json


def load_from_json_file(filename):
    ''' start function '''
    with open(filename, encoding="utf-8") as f:
        read_data = f.read()
    return json.loads(read_data)
