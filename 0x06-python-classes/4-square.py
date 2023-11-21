#!/usr/bin/python3

"""Define a class Square."""

class Square:
    """Represents a square."""

    def __init__(self, size=0):
        """  Initializes a new instance of the Square class.
        
        Args:
            size (int, optional): The size of each side of the square. Defaults to 0.
        """
        self.size = size

    @property
    def size(self):
        """ Getter method to retrieve the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Return area of the square."""
        return self.__size ** 2
