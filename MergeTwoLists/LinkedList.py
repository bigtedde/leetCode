# Ted Lawson 8/1/22

from Node import Node


class LinkedList:

    # Initiates the LinkedList
    def __init__(self):
        self.head = None

    # Prints the linked list
    def print(self):
        if self.head is None:
            print('Linked List is empty.')
        else:
            n = self.head
            while n is not None:
                print(n.data, end=' -> ')
                n = n.ref

    # Links a node to the beginning of a list
    def add_begin(self, data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node

    # Links a node to the end of the list
    def add_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.ref is not None:
                n = n.ref
            n.ref = new_node

    # Links a node after the 1st instance of a node with the passed value.
    def add_after(self, data, x):
        new_node = Node(data)
        n = self.head
        success = False

        while (n.ref is not None) or (n.data == x):
            if n.data == x:
                new_node.ref = n.ref
                n.ref = new_node
                success = True
                return
            else:
                n = n.ref

        if not success:
            print(f'No node "{x}" found. Could not add a link for node "{data}".')
