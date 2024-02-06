#!/usr/bin/python3
"""Square class definition"""


class Square:
    """Defines a square with a given size."""

    def __init__(self, size):
        """Initialize the square with a specific size.

        Args:
            size (int): The size of the square's sides.
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        self._size = size

    @property
    def size(self):
        """Getter method for the size of the square."""
        return self._size

    @size.setter
    def size(self, value):
        """Setter method for the size of the square.

        Args:
            value (int): The new size of the square.
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self._size = value

    def area(self):
        """Compute the area of the square.

        Returns:
            int: The area of the square.
        """
        return self._size ** 2

    def my_print(self):
        """Print the square using '#' characters.

        Prints the square pattern using '#' characters based on the size.
        """
        if self._size == 0:
            print()
        else:
            for _ in range(self._size):
                print("#" * self._size)
