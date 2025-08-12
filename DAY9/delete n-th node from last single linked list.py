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
                return  # n is larger than length
            first = first.next

        # Move both pointers until first reaches the end
        while first is not None:
            first = first.next
            second = second.next
        # Delete target node
        second.next = second.next.next
        # Update root in case first node was deleted
        self.root = dummy.next

# Example usage
a = Singlelinkedlist()
a.addnewnode(10)
a.addnewnode(20)
a.addnewnode(30)
a.addnewnode(40)
a.addnewnode(50)
print("Original list:")
a.display_list()
a.delete_nth_from_end(2)  # Delete 2nd node from end
print("After deleting 2nd node from end:")
a.display_list()