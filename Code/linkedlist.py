#!python
class Node(object):

    def __init__(self, data):
        """Initialize this node with the given data."""
        self.data = data  # Data of the node
        self.next = None  # Acts as a pointer to the next Node

    def __repr__(self):
        """Return a string representation of this node."""
        return 'Node({!r})'.format(self.data)


class LinkedList(object):

    def __init__(self, items=None):
        """Initialize this linked list and append the given items, if any."""
        self.head = None  # First node
        self.tail = None  # Last node
        # Append given items
        if items is not None:
            for item in items:
                self.append(item)

    def __str__(self):
        """Return a formatted string representation of this linked list."""
        items = ['({!r})'.format(item) for item in self.items()]
        return '[{}]'.format(' -> '.join(items))

    def __repr__(self):
        """Return a string representation of this linked list."""
        return 'LinkedList({!r})'.format(self.items())

    def items(self):
        """Return a list (dynamic array) of all items in this linked list.
        Best and worst case running time: O(n) for n items in the list (length)
        because we always need to loop through all n nodes to get each item."""
        items = []  # O(1) time to create empty list
        # Start at head node
        node = self.head  # O(1) time to assign new variable
        # Loop until node is None, which is one node too far past tail
        while node is not None:  # Always n iterations because no early return
            items.append(node.data)  # O(1) time (on average) to append to list
            # Skip to next node to advance forward in linked list
            node = node.next  # O(1) Point to new the new node
        # Now list contains items from all nodes
        return items  # O(1) time to return list

    def is_empty(self):
        """Return a boolean indicating whether this linked list is empty."""
        return self.head is None

    def length(self):
        """Return the length of this linked list by traversing its nodes.
        TODO: Running time: O(???) Why and under what conditions?
        ANS: o(n) because we don't know how many nodes are in the list and it loops"""
        node = self.head
        node_len = 0

        while node is not None:
            node_len += 1
            node = node.next

        return node_len

    def append(self, item):
        """Insert the given item at the tail of this linked list.
        TODO: Running time: O(???) Why and under what conditions?
        ANS: o(1) because it runs through once and doesn't loop"""

        # Creates a new node item with data
        new_node = Node(item)

        if self.is_empty():
            self.head = new_node  # If the node is empty the new_node is the head
            self.tail = new_node  # Makes sure that head and tail points to the one list
        else:
            self.tail.next = new_node
            self.tail = new_node

    def prepend(self, item):
        """Insert the given item at the head of this linked list.
        TODO: Running time: O(???) Why and under what conditions?
        ANS: o(1) because it runs through once and doesn't loop"""

        # Creates a new node item with data
        new_node = Node(item)

        if self.is_empty():
            self.head = new_node  # If the node is empty the new_node is the head
            self.tail = new_node  # Makes sure that head and tail points to the one list
        else:
            new_node.next = self.head  # Assign the new node as the head
            self.head = new_node  # Sets the new_node as the head

    def find(self, quality):
        """Return an quality from this linked list satisfying the given quality.
        TODO: Best case running time: O(???) Why and under what conditions?
        ANS: o(1) If we're looking for the first item it runs once
        TODO: Worst case running time: O(???) Why and under what conditions?
        ANS: o(n) If we don't know where the item is we need to loop"""

        node = self.head
        while node is not None:
            if quality(node.data):
                return node.data
            node = node.next
        return None

    def find_index(self, item):
        """
        This wasn't apart of the starter code

        Returns the index of the item
        BEST: o(1) If the index is the first item, it only runs once
        WORST: o(n) Not sure where the item is, so it must loop"""
        count = 0
        node = self.head
        while node is not None:
            if node.data == item:
                return count
            count += 1
            node = node.next
        return None

    def delete(self, item):
        """Delete the given item from this linked list, or raise ValueError.
        TODO: Best case running time: O(???) Why and under what conditions?
        ANS: o(1) If we're looking for the first item it runs once
        TODO: Worst case running time: O(???) Why and under what conditions?
        ANS: o(n) Because we don't know what item to delete and it uses find_index() which loops.  """

        node = self.head

        if node and node.data == item:
            if self.tail == self.head:  # Handles edge case of 1 item in list
                self.tail = node.next
            self.head = node.next
            return

        while node and node.data != item:
            prev_node = node  # Keeps track of the previous node
            node = node.next

        # Checks if the item was in the linked list
        if node is None:
            raise ValueError(f'Item not found: {item}')

        if self.tail == node:  # Handles case where node to delete is the tail
            self.tail = prev_node

        prev_node.next = node.next


def test_linked_list():
    ll = LinkedList()
    print('list: {}'.format(ll))

    print('\nTesting append:')
    for item in ['A', 'B', 'C']:
        print('\nappend({!r})'.format(item))
        ll.append(item)
        print('list: {}'.format(ll))

    print('\n')

    print('head: {}'.format(ll.head))
    print('tail: {}'.format(ll.tail))
    print('length: {}'.format(ll.length()))

    # Enable this after implementing delete method
    delete_implemented = True
    if delete_implemented:
        print('\nTesting delete:')
        for item in ['B', 'C', 'A']:
            print('\ndelete({!r})'.format(item))
            ll.delete(item)
            print('list: {}'.format(ll))

        print('\nhead: {}'.format(ll.head))
        print('tail: {}'.format(ll.tail))
        print('length: {}'.format(ll.length()))


if __name__ == '__main__':
    test_linked_list()
