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

    def display_reverse(self, node):
        if node is None:
            return
        self.display_reverse(node.next)  # go to end first
        print(node.val, end="->")

# Testing
a = Singlelinkedlist()
a.addnewnode(10)
a.addnewnode(20)
a.addnewnode(30)

print("Normal order:")
a.display_list()

print("Reverse order:")
a.display_reverse(a.root)
print("null")