#!/usr/bin/python3
"""Add all arguments to a Python list and save them to a file"""

import sys
import json
from os import path
from typing import List


def load_from_json_file(filename: str) -> List:
    """Load JSON data from a file"""
    with open(filename, "r") as f:
        return json.load(f)


def save_to_json_file(my_obj: List, filename: str) -> None:
    """Save JSON data to a file"""
    with open(filename, "w") as f:
        json.dump(my_obj, f)
