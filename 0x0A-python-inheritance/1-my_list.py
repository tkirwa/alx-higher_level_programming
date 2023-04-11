#!/usr/bin/python3
"""Module defining MyList class"""


class MyList(list):
    """Inherits from list class"""

    def print_sorted(self):
        """Prints the list, but sorted in ascending order"""
        print(sorted(self))
