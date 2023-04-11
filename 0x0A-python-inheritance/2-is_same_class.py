#!/usr/bin/python3


def is_same_class(obj, a_class):
    """Check if an object is an instance of a specific class.

    Args:
        obj (any): The object to check.
        a_class (type): The class to check against.

    Returns:
        bool: True if obj is an instance of a_class; False otherwise.
    """
    return type(obj) is a_class
