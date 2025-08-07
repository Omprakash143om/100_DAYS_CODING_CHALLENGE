class Queue:
    def __init__(self, capacity):
        self.queue = [0] * capacity
        self.capacity = capacity
        self.front = 0
        self.rear = 0

    def is_full(self):
        return self.rear == self.capacity

    def is_empty(self):
        return self.front == self.rear

    def enqueue(self, data):
        if self.is_full():
            print("Queue is Full")
        else:
            self.queue[self.rear] = data
            print(f"Enqueued: {data}")
            self.rear += 1

    def dequeue(self):
        if self.is_empty():
            print("Queue is Empty")
        else:
            print(f"Dequeued: {self.queue[self.front]}")
            self.front += 1

    def display(self):
        if self.is_empty():
            print("Queue is Empty")
        else:
            print("Queue Elements:", self.queue[self.front:self.rear])

# Testing
q = Queue(5)
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.display()
q.dequeue()
q.display()
