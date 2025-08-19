class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class SingleLinkedList:
    def __init__(self):
        self.root = None
        self.nodes_map = {}   # store value → node reference

    def addnewnode(self, val):
        # if value already exists, create cycle
        if val in self.nodes_map:
            temp = self.root
            while temp.next is not None:
                temp = temp.next
            temp.next = self.nodes_map[val]
            return

        # otherwise add normally
        n = Node(val)
        self.nodes_map[val] = n
        if self.root is None:
            self.root = n
            return
        temp = self.root
        while temp.next is not None:
            temp = temp.next
        temp.next = n

    # Detect Cycle using two pointers
    def hasCycle(self):
        slow = self.root
        fast = self.root
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

# -------- MAIN --------
n = int(input("Enter number of nodes: "))
a = SingleLinkedList()

for i in range(n):
    val = int(input(f"Enter value for node {i+1}: "))
    a.addnewnode(val)

if a.hasCycle():
    print("Cycle detected ✅ (duplicate created a cycle)")
else:
    print("No cycle ❌")
