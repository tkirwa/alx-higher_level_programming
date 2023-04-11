#!/usr/bin/python3
"""Defines a BaseGeometry class."""


class BaseGeometry:
    """Represent base geometry."""

    def area(self):
        """Raise an exception for area is not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate the integer value.

        Args:
            name (str): The name.
            value (int): The value.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
