#!/usr/bin/python3
"""
Module that adds all arguments to a Python list, and then saves them to a file
"""

import json
import sys
from os import path
from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file


if __name__ == "__main__":
    """Executes the script"""

    filename = "add_item.json"
    items = []

    if path.exists(filename):
        items = load_from_json_file(filename)

    items += sys.argv[1:]

    save_to_json_file(items, filename)
