#5c)Write a program to demonstrate the implementation of a queue using a linked list (using the enqueue and 
#   dequeue functions)


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, data):
        new_node = Node(data)
        if self.rear is None:
            self.front = self.rear = new_node
            return
        self.rear.next = new_node
        self.rear = new_node

    def dequeue(self):
        if self.front is None:
            return "Queue Underflow"
        temp = self.front
        self.front = temp.next
        if self.front is None:
            self.rear = None
        return temp.data

    def display(self):
        current = self.front
        if current is None:
            print("Queue is empty")
            return
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

q = Queue()

q.enqueue("Range Rover")
q.enqueue("G Wagon")
q.enqueue("Urus")

print("Queue after Enqueue:")
q.display()

print("\nDequeued element:", q.dequeue())
print("Dequeued element:", q.dequeue())

print("\nQueue after Dequeue:")
q.display()

print("\nDequeued element:", q.dequeue())
print("Dequeued element:", q.dequeue())