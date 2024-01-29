#!/usr/bin/python3
"""Defines a Rectangle class."""


class Rectangle:
    """first trigger point in the class
            that define both height and width."""
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        type(self).number_of_instances += 1
        self.width = width
        self.height = height

    """ width assigning and getting value."""

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    """ height assigning and getting value """

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    """ calculating area """

    def area(self):
        return self.__width * self.__height

    """ calculating perimeter """

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    """note that here we use the __str__
        just to print in readable form
        <3-rectangle.Rectangle object at 0x7f92a75a2eb8>
        and we used repr to print the return value
        as it return from __str__ in the main fun"""

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""
        """ then here we print #
            by checking every height and width
            and based on the height will assign
            how many raw print and width how many
            columns will print """
        result = []
        for i in range(self.__height):
            [result.append('#') for j in range(self.__width)]
            if i != self.__height - 1:
                result.append("\n")
        return "".join(result)

    def __repr__(self):
        """return the string representation of the class."""
        return_str = "Rectangle(" + str(self.__width)
        return_str += ", " + str(self.__height) + ")"
        return return_str

    def __del__(self):
        """Print a message for every deletion of a Rectangle."""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
