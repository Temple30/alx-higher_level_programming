#!/usr/bin/python3
"""Singly-linked definition"""


class Node:
    """Represents a node in a singly-linked list."""

    def __init__(self, data, next_node=None):
        """Initialize a node.

        Args:
            data (int): The data of the node.
            next_node (Node, optional): The next node in the list. Defaults to None.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Getter and setter for the data of the node."""
        return self.__data

    @data.setter
    def data(self, value):
        """Set the data of the node.

        Args:
            value (int): The new data of the node.

        Raises:
            TypeError: If value is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Getter and setter for the next node."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Set the next node of the current node.

        Args:
            value (Node or None): The next node in the list.

        Raises:
            TypeError: If value is not a Node object or None.
        """
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object or None")
        self.__next_node = value


class SinglyLinkedList:
    """Represents a singly-linked list."""

    def __init__(self):
        """Initialize an empty singly-linked list."""
        self.__head = None

    def sorted_insert(self, value):
        """Insert a new node into the list in sorted order.

        Args:
            value (int): The value to insert into the list.
        """
        new_node = Node(value)
        if self.__head is None or self.__head.data >= value:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            current = self.__head
            while current.next_node and current.next_node.data < value:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        """Return a string representation of the linked list."""
        values = []
        current = self.__head
        while current:
            values.append(str(current.data))
            current = current.next_node
        return '\n'.join(values)
