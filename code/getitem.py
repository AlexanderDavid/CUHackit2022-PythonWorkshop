from typing import Any

class Node:
    def __init__(self, datum: Any=None):
        self.datum = None # type: Any
        self.next = None # type: Node

class LinkedList:
    def __init__(self):
        self.root = Node()

    def append(self, value: Any):
        tmp = self.root
        while tmp.next is not None:
            tmp = tmp.next

        new = Node(value)
        tmp.next = new

    def __getitem__(self, key: int) -> Any:
        tmp = self.root
        i = 0
        while tmp.next is not None:
            i += 1
            tmp = tmp.next

            if i == key:
                return tmp.datum

        raise IndexError()

    def __delitem__(self, key: int) -> Node:
        tmp = self.root
        i = 0
        while tmp.next is not None:
            i += 1
            tmp = tmp.next

            if i == key:
                if tmp.next.next is not None:
                    tmp.next = tmp.next.next
                else:
                    tmp.next = None

        raise IndexError()
