#!/usr/bin/python3
''' module python3 '''
import json
import sys

if __name__ == "__main__":
    load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    
    list_args = sys.argv[1:]
    filename = "add_item.json"
    
    try:
        list_args = list(load_from_json_file(filename)) + list_args
    except FileNotFoundError:
        save_to_json_file([], filename)
        exit()
    
    save_to_json_file(list_args, filename)
