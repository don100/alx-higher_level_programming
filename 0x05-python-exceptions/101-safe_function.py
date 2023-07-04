#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        if fct is None or args is None:
            raise Exception
        return fct(args[0], args[1])
    except Exception as e:
        print(f"Exception: {e}", file=sys.stderr)
        return None
