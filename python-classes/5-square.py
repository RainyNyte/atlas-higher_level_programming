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
        self.size = size

    @property
    def size(self):
        """Gets the size of the square.
        Returns:
            int: the size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the square.
        Args:
            value (int): size of one side of the square.
        Raises:
            TypeError: if value is not an integer.
            ValueError: if value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculates the area of the square.
        Returns:
            int: the area of the square, equal to it's size squared
        """
        return self.__size ** 2

    def my_print(self):
        """prints a square using the # character, 
        prints an empty line if size is 0
        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print("#" * self.__size)
