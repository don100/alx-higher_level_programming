#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        a = fct(args[0], args[1])
        return a
    except Exception as e:
        print(f"Exception: {e}", file=sys.stderr)
        return None
