class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class Singlelinkedlist:
    def __init__(self):
        self.root = None

    def addnewnode(self, val):
        n = Node(val)
        if self.root is None:
            self.root = n
            return
        temp = self.root
        while temp.next is not None:
            temp = temp.next
        temp.next = n

    def display_list(self):
        temp = self.root
        while temp is not None:
            print(temp.val, end="->")
            temp = temp.next
        print("null")

    def delete_nth_from_end(self, n):
        dummy = Node(0)
        dummy.next = self.root
        first = dummy
        second = dummy
        # Move first pointer n+1 steps ahead
        for _ in range(n + 1):
            if first is None:
                print("N is larger than the length of the list")
                return
            first = first.next
        # Move both pointers until first reaches the end
        while first is not None:
            first = first.next
            second = second.next
        # Delete target node
        second.next = second.next.next
        # Update root in case first node was deleted
        self.root = dummy.next

a = Singlelinkedlist()
# Take number of nodes
num_nodes = int(input("Enter number of nodes: "))
for i in range(num_nodes):
    value = int(input(f"Enter value for node {i+1}: "))
    a.addnewnode(value)
print("\nOriginal list:")
a.display_list()
# Take n (node to delete from end)
n = int(input("\nEnter n (node position from end to delete): "))
a.delete_nth_from_end(n)
print("\nList after deletion:")
a.display_list()