#!/usr/bin/python3
import sys
"""class Node"""


class Node:
    """Content class Node."""
    def __init__(self, data, next_node=None):
        if type(data) != int:
            raise Exception("data must be an integer")
        if next_node is not None and type(next_node) != Node:
            raise Exception("next_node must be a Node object")
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if type(value) != int:
            raise Exception("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if value is not None and type(value) != Node:
            raise Exception("next_node must be a Node object")
        self.__next_node = value


"""class SinglyLinkedList"""


class SinglyLinkedList:
    """Content class SinglyLinkedList."""
    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        new_node = Node(value)
        current = self.__head
        prev = None

        if self.__head is None:
            self.__head = new_node
        else:
            while current.next_node is not None:
                if current.data >= value:
                    new_node.next_node = current
                    if prev is None:
                        new_node.next_node = current
                        self.__head = new_node
                        current = None
                    else:
                        current = prev
                    break
                prev = current
                current = current.next_node
            if current is not None:
                current.next_node = new_node

    def __str__(self):
        all_data = ""
        current = self.__head
        while current is not None:
            sys.stdout.write(f"{str(current.data)}\n")
            current = current.next_node
        return ''
