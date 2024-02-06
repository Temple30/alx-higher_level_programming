#!/usr/bin/python3
"""Square class definition"""


class Square:
    """Represents a square."""

    def __init__(self, size=0):
        """Initialize a square with a given size.

        Args:
            size (int): The length of a side of the square (default is 0).
        """
        self.__size = size

    @property
    def size(self):
        """Getter and setter for the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square.

        Args:
            value (int): The length of a side of the square.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is negative.
        """
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """Calculate the area of the square."""
        return self.__size ** 2

    def __le__(self, other):
        """Less than or equal comparison."""
        return self.area() <= other.area()

    def __lt__(self, other):
        """Less than comparison."""
        return self.area() < other.area()

    def __ge__(self, other):
        """Greater than or equal comparison."""
        return self.area() >= other.area()

    def __ne__(self, other):
        """Not equal comparison."""
        return self.area() != other.area()

    def __gt__(self, other):
        """Greater than comparison."""
        return self.area() > other.area()

    def __eq__(self, other):
        """Equal comparison."""
        return self.area() == other.area()
