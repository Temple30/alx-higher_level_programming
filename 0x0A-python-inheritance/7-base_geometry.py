#!/usr/bin/python3

"""Defines class BaseGeometry."""


class BaseGeometry:
    """Represents a basic geometric shape."""

    def area(self):
        """Calculate the area of the geometric shape.

        Raises:
            Exception: This method is not implemented in the base class.
        """
        raise Exception("area() is not implemented")
