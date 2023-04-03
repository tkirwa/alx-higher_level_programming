#!/usr/bin/python3
"""
Module 7-rectangle
Defines a Rectangle class.
"""


class Rectangle:
    """Represents a rectangle."""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initializes a new rectangle.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __del__(self):
        """Deletes the rectangle and decrements the number of instances."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @property
    def width(self):
        """Gets the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width of the rectangle.

        Args:
            value (int): The new width of the rectangle.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Gets the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of the rectangle.

        Args:
            value (int): The new height of the rectangle.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """Computes the area of the rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Computes the perimeter of the rectangle."""
        return (self.width + self.height) * 2 if self.width and self.height else 0

    def __str__(self):
    """Returns a string representation of the rectangle."""
    row = str(self.print_symbol) * self.width
    return "\n".join([row] * self.height)


    def __repr__(self):
        """Returns a string representation of the rectangle for recreation."""
        return f"Rectangle({self.width}, {self.height})"
