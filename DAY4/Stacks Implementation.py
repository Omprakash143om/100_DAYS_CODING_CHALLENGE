class Stack:
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)
        print(f"Pushed: {data}")

    def pop(self):
        if not self.is_empty():
            print(f"Popped: {self.stack.pop()}")
        else:
            print("Stack is empty")

    def peek(self):
        if not self.is_empty():
            print(f"Top element: {self.stack[-1]}")

    def is_empty(self):
        return len(self.stack) == 0
    
    def display(self):
        print("Stack contents:", self.stack)

s = Stack()
s.push(10)
s.push(20)
s.push(30)
s.display()
s.pop()
s.display()
s.peek()
s.display()

