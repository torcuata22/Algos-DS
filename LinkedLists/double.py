class DoubleNode:
    def __init__(self, value):
        self.value = value
        self.next = None #next node
        self.prev = None #previous node


class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, value): #this method allows the class to gain nodes
        new_node = DoubleNode(value)

        if self.head is None: #if the list is empty this block runs
            self.head = new_node
            self.tail = new_node #link to the tail
            print("Head Node created: ", self.head.value)
            return

       #this is the code to handle the append operation
        new_node.prev = self.tail
        self.tail.next = new_node
        self.tail = new_node 
        print("Head Node created: ", self.head.value)
        return


dllist = DoubleLinkedList()
dllist.append("First Node")
