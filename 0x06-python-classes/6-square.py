#!/usr/bin/python3
# 6-square.py
# Nasser Eldin <MrWolf0>
"""Define a class Square."""


class Square:
    """Represent a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new Square.

                Args:
                    size (int): The size of the new square.
                """
        self.size = size
        self.position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        """ this condition check for 3 condition as
        1 - for the object is tuple or not
        2- if it is a tuple check the if it is 2 elements
         or not .
         3- if the integer + or - by using all function
         that check the value that passed to the setter then
         check if it is an integer then
         using any function to check if any number < 0"""
        if (
                not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(i, int) for i in value) or
                any(i < 0 for i in value)
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        return self.__size * self.__size

    def my_print(self):
        """Print the square with the character '#' and
        considering the position."""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
