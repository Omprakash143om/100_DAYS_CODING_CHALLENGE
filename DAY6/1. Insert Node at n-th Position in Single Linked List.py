class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class SingleLinkedList:
    def __init__(self):
        self.root = None

    def addnewnode(self, val):
        """Add a node at the end of the list"""
        n = Node(val)
        if self.root is None:
            self.root = n
            return
        temp = self.root
        while temp.next is not None:
            temp = temp.next
        temp.next = n

    def insert_at_position(self, pos, val):
        """Insert a node at the given position (1-based index)"""
        new_node = Node(val)

        # If inserting at the beginning
        if pos == 1:
            new_node.next = self.root
            self.root = new_node
            return

        temp = self.root
        count = 1
        while temp is not None and count < pos - 1:
            temp = temp.next
            count += 1

        if temp is None:
            print("Position out of range")
            return

        new_node.next = temp.next
        temp.next = new_node

    def display_list(self):
        temp = self.root
        while temp is not None:
            print(temp.val, end="->")
            temp = temp.next
        print("null")


# Example usage
a = SingleLinkedList()
a.addnewnode(10)
a.addnewnode(20)
a.addnewnode(30)
print("Original List:")
a.display_list()

a.insert_at_position(2, 15)  # Insert 15 at position 2
print("After Insertion at position 2:")
a.display_list()
