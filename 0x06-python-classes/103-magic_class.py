#!/usr/bin/python3
"""Magic class implementation for a circle."""

import math

class MagicClass:
    """Represents a circle with magic calculations."""

    def __init__(self, radius=0):
        """Initialize the MagicClass with a radius.

        Args:
            radius (int or float, optional): The radius of the circle. Defaults to 0.

        Raises:
            TypeError: If radius is not a number.
        """
        if not isinstance(radius, (int, float)):
            raise TypeError("radius must be a number")
        self.__radius = float(radius)

    def area(self):
        """Calculate the area of the circle.

        Returns:
            float: The area of the circle.
        """
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """Calculate the circumference of the circle.

        Returns:
            float: The circumference of the circle.
        """
        return 2 * math.pi * self.__radius
