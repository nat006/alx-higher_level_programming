#!/usr/bin/python3
"""Define a class square."""

class Square:
    """Represents a square."""

    def __init__(self, size=0):
        """  Initializes a new instance of the Square class.
        
        Args:
            size (int): The size of each side of the square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Return area of the square."""
        return self.__size ** 2
