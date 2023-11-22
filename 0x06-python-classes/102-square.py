#!/usr/bin/python3
class Square:
    """
    Represents a square.

    Attributes:
        __size (float or int): The size of each side of the square.
    """

    def __init__(self, size=0):
        """
        Initializes a new instance of the Square class.

        Args:
            size (float or int, optional): The size of each side of the square. Defaults to 0.
        """
        self.size = size

    @property
    def size(self):
        """
        Getter method to retrieve the size of the square.

        Returns:
            float or int: The size of each side of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method to set the size of the square.

        Args:
            value (float or int): The size of each side of the square.

        Raises:
            TypeError: If the value is not a number.
            ValueError: If the value is less than 0.
        """
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """
        Calculates and returns the area of the square.

        Returns:
            float or int: The area of the square.
        """
        return self.size ** 2

    def __eq__(self, other):
        """
        Checks if two Square instances have equal areas.

        Args:
            other (Square): The other Square instance to compare with.

        Returns:
            bool: True if the areas are equal, False otherwise.
        """
        return self.area() == other.area()

    def __ne__(self, other):
        """
        Checks if two Square instances have different areas.

        Args:
            other (Square): The other Square instance to compare with.

        Returns:
            bool: True if the areas are different, False otherwise.
        """
        return self.area() != other.area()

    def __gt__(self, other):
        """
        Checks if the area of the current Square instance is greater than the area of another Square instance.

        Args:
            other (Square): The other Square instance to compare with.

        Returns:
            bool: True if the area is greater, False otherwise.
        """
        return self.area() > other.area()

    def __ge__(self, other):
        """
        Checks if the area of the current Square instance is greater than or equal to the area of another Square instance.

        Args:
            other (Square): The other Square instance to compare with.

        Returns:
            bool: True if the area is greater than or equal, False otherwise.
        """
        return self.area() >= other.area()

    def __lt__(self, other):
        """
        Checks if the area of the current Square instance is less than the area of another Square instance.

        Args:
            other (Square): The other Square instance to compare with.

        Returns:
            bool: True if the area is less, False otherwise.
        """
        return self.area() < other.area()

    def __le__(self, other):
        """
        Checks if the area of the current Square instance is less than or equal to the area of another Square instance.

        Args:
            other (Square): The other Square instance to compare with.

        Returns:
            bool: True if the area is less than or equal, False otherwise.
        """
        return self.area() <= other.area()
