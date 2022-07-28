class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None  # creates a class with constructor that initializes head to None

    def append(self, value):  #adds nodes to LinkedList object of this class
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            print("Head Node created: ", self.head.value)
            return

        node = self.head
        while node.next is not None:
            node = node.next

        node.next = new_node
        print("Appended new Node with value: ", node.next.value)
        
    def prepend(self,value):
        new_node = Node(value)
        
        if self.head is None:
            self.head = new_node
            print("Head Node created: ", self.head.value)
            return
        else:
            prev_head = self.head.value
            self.head = new_node
            self.head.next = prev_head
            print("Prepend new Head node with value: ", self.head.value)
            print("Second Node is: ", self.head.next)
            
llist = LinkedList()
llist.prepend("First Node")
llist.prepend("Second Node")
llist.prepend("Third Node")
llist.prepend("Fourth Node")

