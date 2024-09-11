#!/usr/bin/python3
"""Module that defines a class that represents a square"""


class Square:
    """Class that represents a square
    
    Attributes:
        __size (int): the size of one side of the square
    """
    def __init__(self, size):
        """Initializes the new Square instance with the given size

        Args:
            size (int): The size of one side of the square
        """
        self.size = size
