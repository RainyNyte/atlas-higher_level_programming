#!/usr/bin/python3
"""Module that defines a class that represents a square."""


class Square:
    """Class that represents a square.
    Attributes:
        __size (int): the size of one side of the square.
        __position (tuple): position of the square as (x,y)
    """
    def __init__(self, size=0, position=(0, 0)):
        """Initializes the new Square instance with the given size.
        Args:
            size (int): The size of one side of the square.
            position (tuple): the position of the square.
        Raises:
            TypeError: If size not int or position not tuple of 2 positive ints.
            ValueError: If size less than 0 or any postion value is negative.
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Gets the position of the square.
        Returns:
            tuple: The position of the square as (x,y)
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Sets the position of the square.
        Args:
            value (tuple): The position of the square as (x,y).
        Raises:
            TypeError: if value is not a tuple of 2 positive integers.
            ValueError: if any value of the tuple is negative.
        """
        if (not isinstance(value, tuple) or
            len(value) != 2 or
            not all(isinstance(i, int) for i in value) or
            not all(i >= 0 for i in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
        
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
            for i in range(self.__position[1]):
                print()
            for i in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
