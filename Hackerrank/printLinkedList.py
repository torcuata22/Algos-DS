#create node:
class singlyLinedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None
#create list:      
class singlyLinkedList:
    def __init__ (self):
        self.head = None
        self.tail= None
    #to insert new nodes    
    def insert_node(self, node_data):
        node = singlyLinkedList(node_data)
        #new node becomes the new head
        if not self.head:
            self.head = node
        #end of linked list (not the head)
        else:
            self.tail.next = node
        self.tail = node
    
def printLinkedList(head):
    current = head #iterates through the list as long as there is a head.
    while current:
        print(current.data)
        current = current.next