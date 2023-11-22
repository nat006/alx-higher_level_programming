#!/usr/bin/python3
class Square:
    """
    Represents a square.
    
    Attributes:
        __size (int): The size of each side of the square.
    """

    def __init__(self, size=0):
        """
        Initializes a new instance of the Square class.
        
        Args:
            size (int, optional): The size of each side of the square. Defaults to 0.
        """
        self.size = size

    @property
    def size(self):
        """
        Getter method to retrieve the size of the square.
        
        Returns:
            int: The size of each side of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method to set the size of the square.
        
        Args:
            value (int): The size of each side of the square.
        
        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """
        Calculates and returns the area of the square.
        
        Returns:
            int: The area of the square.
        """
        return self.size ** 2

    def my_print(self):
        """
        Prints the square with the character '#' to stdout.
        If size is equal to 0, prints an empty line.
        """
        if self.size == 0:
            print()
        else:
            for _ in range(self.size):
                print("#" * self.size)
