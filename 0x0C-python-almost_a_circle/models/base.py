#!/usr/bin/python3
class Base:
    __nb_objects = 0  # private class attribute

def __init__(self, id=None):
    if id is not None:
        self.id = id  # if id is provided, assign it
else:
    Base.__nb_objects += 1  # increment the counter
self.id = Base.__nb_objects  # assign the new value to id
