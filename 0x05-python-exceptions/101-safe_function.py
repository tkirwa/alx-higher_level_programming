#!/usr/bin/python3
"""
safe_function module

Contains function that executes a function safely
"""

import sys


def safe_function(fct, *args):
    try:
        result = fct(*args)
        return result
    except Exception as error:
        print("Exception: {}".format(error), file=sys.stderr)
        return None