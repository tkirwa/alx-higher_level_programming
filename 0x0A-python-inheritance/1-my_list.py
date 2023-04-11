#!/usr/bin/python3
"""Module that contains the MyList class that inherits from list"""


class MyList(list):
    """
    A class that inherits from list and adds a print_sorted method.

    Attributes:
        Inherits from list.

    Methods:
        print_sorted(self): prints the list, but sorted (ascending sort).
    """

    def print_sorted(self):
        """Prints the list, but sorted (ascending sort)"""
        print(sorted(self))
