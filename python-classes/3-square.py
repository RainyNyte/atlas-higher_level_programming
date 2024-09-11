#!/usr/bin/python3
"""Module that defines a class that represents a square."""


class Square:
    """Class that represents a square.
    Attributes:
        __size (int): the size of one side of the square.
    """
    def __init__(self, size=0):
        """Initializes the new Square instance with the given size.
        Args:
            size (int): The size of one side of the square.
        Raises:
            TypeError: If size not an integer.
            ValueError: If size less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Calculates the area of the square.
        Returns:
            int: the area of the square, equal to it's size squared
        """
        return self.__size ** 2
