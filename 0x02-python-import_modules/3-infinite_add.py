#!/usr/bin/env python3

# 3-infinite_add.py

if __name__ == "__main__":

    """Print the addition of all arguments."""
    
    import sys

    args = sys.argv[1:]
    result = 0
    for arg in args:
        result += int(arg)
    print(result)
