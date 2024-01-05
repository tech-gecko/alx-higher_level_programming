#!/usr/bin/python3
""" This module contains the class, 'Rectangle'. """


class Rectangle:
    """ This class defines a rectangle and all it's properties. """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        else:
            self.__width = value

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >= 0')
        else:
            self.__height = value

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)
        if self.width != 0 and self.height != 0 else 0

    def draw_rectangle(self):
        result = ""
        for i in range(self.height):
            for j in range(self.width):
                result += "#"
            result += "\n"
        return result

    def __str__(self):
        return self.draw_rectangle()
