#!/usr/bin/python3


def lookup(obj):
    """
    Returns the list of available attributes and methods of an object.

    Args:
        obj (object): The object to lookup.

    Returns:
        A list of strings representing the available attributes and methods of the object.
    """
    return [attr for attr in dir(obj)]
