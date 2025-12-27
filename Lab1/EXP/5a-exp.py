#5a) Write a program to create a linked list and display its elements


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def display(self):
        current = self.head
        if current is None:
            print("The list is empty.")
            return

        print("Linked List elements:")
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

my_list = LinkedList()

my_list.append("Tesla Model S")
my_list.append("Lucid Air")
my_list.append("Porsche Taycan")
my_list.append("Audi e-tron")

my_list.display()