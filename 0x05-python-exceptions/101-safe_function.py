#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        return fct(int(args[0]), int(args[1]))
    except Exception as e:
        print(f"Exception: {e}", file=sys.stderr)
        return None
