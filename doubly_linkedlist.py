
class Node(object):

    def __init__(self, data):
        """Initialize this node with the given data."""
        self.data = data
        self.prev = None
        self.next = None

    def __repr__(self):
        """Return a string representation of this node."""
        return 'Node({!r})'.format(self.data)


class DoublyLinkedList(object):

    def __init__(self, iterable=None):
        """Initialize this linked list and append the given items, if any."""
        self.head = None  # First node
        self.tail = None  # Last node
        self.size = 0  # Number of nodes
        self.node_count = 0
        # Append the given items
        if iterable is not None:
            for item in iterable:
                self.append(item)

    def __str__(self):
        """Return a formatted string representation of this linked list."""
        items = ['({!r})'.format(item) for item in self.items()]
        return '[{}]'.format(' -> '.join(items))

    def __repr__(self):
        """Return a string representation of this linked list."""
        return 'DoublyLinkedList({!r})'.format(self.items())

    def items(self):
        """Return a list of all items in this linked list.
        Best and worst case running time: Theta(n) for n items in the list
        because we always need to loop through all n nodes."""
        # Create an empty list of results
        result = []  # Constant time to create a new list
        # Start at the head node
        node = self.head  # Constant time to assign a variable reference
        # Loop until the node is None, which is one node too far past the tail
        while node is not None:  # Always n iterations because no early exit
            # Append this node's data to the results list
            result.append(node.data)  # Constant time to append to a list
            # Skip to the next node
            node = node.next  # Constant time to reassign a variable
        # Now result contains the data from all nodes
        return result  # Constant time to return a list

    def is_empty(self):
        """Return True if this linked list is empty, or False."""
        return self.head is None

    def length(self):
        # TODO: add efficient way to keep track of nodes: within the append and remove function
        return self.size
        
    def get_at_index(self, index):
        """Return the item at the given index in this linked list, or
        raise ValueError if the given index is out of range of the list size.
        Best case running time: O(1) under what conditions? is constant time to retrieve the end or beginning index
        Worst case running time: O(n) under what conditions? if the index is right before the last index"""
        # Check if the given index is out of range and if so raise an error
        if not (0 <= index < self.size):
            raise ValueError('List index out of range: {}'.format(index))

        # TODO: Find the node at the given index and return its data

        if index == 0:
            return self.head.data
        elif index == self.size - 1:
            return self.tail.data
        else:
            node = self.head
            print(node.data)
            for i in range(index+1):
                print(node.data)
                if i == index:
                    return node.data
                node = node.next

    def insert_at_index(self, index, item):
        """Insert the given item at the given index in this linked list, or
        raise ValueError if the given index is out of range of the list size.
        Best case running time: O(1) under what conditions? When you are inserting at the beginning or at the end of the linkedlist
        Worst case running time: O(n) under what conditions? When you are inserting at the index right before the last index"""
        # Check if the given index is out of range and if so raise an error
        if not (0 <= index <= self.size):
            raise ValueError('List index out of range: {}'.format(index))
        # TODO: Find the node before the given index and insert item after it
        
        if index == 0:
            self.prepend(item)

        elif index == self.size:
            self.append(item)
            
        else:
            new_node = Node(item)
            node = self.head
            prev = None

            for i in range(index-1):
                prev = node
                node = node.next

            prev.next = new_node
            new_node.next = node
            self.size += 1
            

    def append(self, item):
        """Insert the given item at the tail of this linked list.
        Best and worst case run time: O(1) because we have access to the tail so we did not have to traverse through the
            whole list to get to the end """
        # Create a new node to hold the given item
        new_node = Node(item)
        # Check if this linked list is empty
        if self.is_empty():
            # Assign head to new node
            # new_node.prev = None
            self.head = new_node
        else:
            # Otherwise insert new node after tail
            new_node.prev = self.tail
            self.tail.next = new_node
        # Update tail to new node regardless
        self.tail = new_node
        self.size += 1

    def prepend(self, item):
        """Insert the given item at the head of this linked list.
        Best and worst case running time: O(1) under what conditions? since we are only changing variables"""
        # Create a new node to hold the given item
        self.size += 1

        new_node = Node(item)

        # Check if this linked list is empty
        if self.is_empty():
            # Assign tail to new node
            self.tail = new_node
        else:
            # Otherwise insert new node before head
            new_node.next = self.head
            self.head.prev = new_node
        # Update head to new node regardless
        self.head = new_node

    def find(self, quality):
        """Return an item from this linked list satisfying the given quality.
        Best case running time: Omega(1) if item is near the head of the list.
        Worst case running time: O(n) if item is near the tail of the list or
        not present and we need to loop through all n nodes in the list."""
        # Start at the head node
        node = self.head  # Constant time to assign a variable reference
        # Loop until the node is None, which is one node too far past the tail
        while node is not None:  # Up to n iterations if we don't exit early
            # Check if this node's data satisfies the given quality function
            if quality(node.data):  # Constant time to call quality function
                # We found data satisfying the quality function, so exit early
                return node.data  # Constant time to return data
            # Skip to the next node
            node = node.next  # Constant time to reassign a variable
        # We never found data satisfying quality, but have to return something
        return None  # Constant time to return None

    def replace(self, old_item, new_item):
        """Replace the given old_item in this linked list with given new_item
        using the same node, or raise ValueError if old_item is not found.
        Best case running time: O(1) under what conditions? if replacing the old item
        Worst case running time: O(n) under what conditions? if the replaced item is the one before the tail"""
        # TODO: Find the node containing the given old_item and replace its
        # data with new_item, without creating a new node object
        node = self.head

        while node != None:
            if node.data == old_item:
                node.data = new_item
                return
            node = node.next

        raise ValueError('item not in lists: {}'.format(old_item))

    def delete_index(self, index):
        """Delete and return the node at the given index, or raise ValueError"""
        node = self.head
        self.size -= 1

        if index == 0:
            # index is the head
            self.head = node.next
            node.prev = None
            return
        elif index == self.size:
            # index is the tail
            self.tail = self.tail.prev
            self.tail.prev.next = None
            return
        else:
            for i in range(index):
                node = node.next

            node.prev.next = node.next
            node.next.prev = node.prev
            return

        raise ValueError('index out of bounds: {}'.format(index))



    def delete(self, item):
        """Delete the given item from this linked list, or raise ValueError.
        Best case running time: O(1) if deleting head and tail of the linked list
        Worst case running time: O(n) under what conditions? if deleting items within the linkedlist. invloves in looping over the linkedlist"""
        

        self.size -= 1

        deleted_node = Node(item)

        if self.head == deleted_node and self.tail == deleted_node:
            self.head = None
            self.tail = None
            return
        elif self.head == deleted_node:
            # deleting the head
            self.head.next.prev = None
            self.head = self.head.next
            return
        elif self.tail == deleted_node:
            # deleting tail
            self.tail.prev.next = None
            self.tail = self.tail.prev
            return
        else:

            node = self.head

            while node != None:
                if node.data == item:
                    if self.head == node:
                        if node.next == None:
                            self.head = None
                            self.tail = None
                        else:
    	                    self.head = node.next
                        return
                    elif self.tail == node:
                        self.tail = node.prev
                        self.tail.next = None
                        return
                    else:
    	                node.prev.next = node.next
    	                node.next.prev = node.prev
                    	return
                else:
                    node = node.next
	    
            else:
    	        # Otherwise raise an error to tell the user that delete has failed
                raise ValueError('Item not found: {}'.format(item))

ll = DoublyLinkedList(['A', 'B', 'C'])
print(ll)
print("head: {}".format(ll.head))
print("head previous: {}".format(ll.head.prev))
print("head next: {}".format(ll.head.next))
print("tail: {}".format(ll.tail))
print("tail previous: {}".format(ll.tail.prev))
print("tail next: {}".format(ll.tail.next))

print("\n")
ll.append('D')
print(ll)
print("head: {}".format(ll.head))
print("head previous: {}".format(ll.head.prev))
print("head next: {}".format(ll.head.next))
print("tail: {}".format(ll.tail))
print("tail previous: {}".format(ll.tail.prev))
print("tail next: {}".format(ll.tail.next))

print("\n")
ll.delete('D')
print(ll)
print("head: {}".format(ll.head))
print("head previous: {}".format(ll.head.prev))
print("head next: {}".format(ll.head.next))
print("tail: {}".format(ll.tail))
print("tail previous: {}".format(ll.tail.prev))
print("tail next: {}".format(ll.tail.next))

ll.append('D')
print("\nStarting loop over doubly linked list")
print(ll)
node = ll.head
while node != None:
	print("on node: {}".format(node.data))
	print("node's next: {}".format(node.next))
	print("node's prev: {}".format(node.prev))
	print("\n")
	node = node.next

print("head: {}".format(ll.head))
print("head previous: {}".format(ll.head.prev))
print("head next: {}".format(ll.head.next))
print("tail: {}".format(ll.tail))
print("tail previous: {}".format(ll.tail.prev))
print("tail next: {}".format(ll.tail.next))


