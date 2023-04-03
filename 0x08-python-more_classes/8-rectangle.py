#!/usr/bin/python3
"""
Module: 8-rectangle.py
"""


class Rectangle:
    """
    Rectangle class

    Args:
        width (int): Width of rectangle. Defaults to 0.
        height (int): Height of rectangle. Defaults to 0.

    Attributes:
        number_of_instances (int): Number of active Rectangle instances.
        print_symbol (Any): Symbol used for string representation.

    Raises:
        TypeError: If either width or height is not an integer.
        ValueError: If either width or height is less than 0.

    Methods:
        area(self): Returns the area of the rectangle.
        perimeter(self): Returns the perimeter of the rectangle.
        __str__(self): Returns a string representation of the rectangle.
        __repr__(self): Returns a string representation of the rectangle that can be used to create a new instance.
        __del__(self): Prints a message when the instance is deleted.
        bigger_or_equal(rect_1, rect_2): Returns the biggest rectangle based on the area.

    Properties:
        width(self): Retrieves the value of width.
        width(self, value): Sets the value of width.
        height(self): Retrieves the value of height.
        height(self, value): Sets the value of height.
    """

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """ Initializes a new instance of Rectangle class """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def area(self):
        """ Calculates the area of the rectangle """
        return self.width * self.height

    def perimeter(self):
        """ Calculates the perimeter of the rectangle """
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """ Returns a string representation of the rectangle """
        if self.width == 0 or self.height == 0:
            return ''
        symbol = str(Rectangle.print_symbol)
        rectangle = []
        for i in range(self.height):
            rectangle.append(symbol * self.width)
        return '\n'.join(rectangle)

    def __repr__(self):
        """ Returns a string representation of the rectangle that can be used to create a new instance """
        return f'Rectangle({self.width}, {self.height})'

    def __del__(self):
        """ Prints a message when the instance is deleted """
        Rectangle.number_of_instances -= 1
        print('Bye rectangle...')

    @property
    def width(self):
        """ Retrieves the value of width """
        return self.__width

    @width.setter
    def width(self, value):
        """ Sets the value of width """
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """ Retrieves the value of height """
        return self.__height

    @height.setter
    def height(self, value):
        """ Sets the value of height """
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ Returns the biggest rectangle based on the area """
        if not isinstance(rect_1, Rectangle):
            raise
