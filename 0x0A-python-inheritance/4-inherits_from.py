#!/usr/bin/python3
"""Defines an inherited class-checking method."""


def inherits_from(obj, a_class):
    """Checks if an object is an inherited instance of a class.
    Args:
        obj (any): The object to check.
        a_class (type): The class to compare.
    Returns:
        A boolean of inheritance.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class

