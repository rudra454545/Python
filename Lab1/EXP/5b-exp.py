#5b)Write a program to demonstrate the implementation of a stack using a linked list (using push and pop 
#   functions)



class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.top is None:
            return "Stack Underflow"
        popped_data = self.top.data
        self.top = self.top.next
        return popped_data

    def display(self):
        current = self.top
        if current is None:
            print("Stack is empty")
            return
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

my_stack = Stack()

my_stack.push("Pagani Huayra")
my_stack.push("Koenigsegg Jesko")
my_stack.push("Bugatti Chiron")

print("Current Stack:")
my_stack.display()

print("\nPopping element:", my_stack.pop())
print("Popping element:", my_stack.pop())

print("\nStack after pop operations:")
my_stack.display()

print("\nPopping element:", my_stack.pop())
print("Popping element:", my_stack.pop())