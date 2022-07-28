class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        


class LinkedList:
    def __init__(self):
       self.head = None
    
    def append(self, value):
        new_node = Node(value)
        
        #for empty list:
        if self.head is None:
            self.head = new_node
            print("Head Node created: ", self.head.value)
            return
        
        node = self.head
        while node.next is not None:
            node = node.next
            
        node.next = new_node
        print("Appended new Node with value " , node.next.value)
        
        
llist = LinkedList()
llist.append(1)
llist.append(2)
llist.append(3)
        
         


