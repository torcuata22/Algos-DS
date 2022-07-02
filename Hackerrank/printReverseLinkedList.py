
        
class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node


        self.tail = node

def print_singly_linked_list(node, sep):
    while node: 
        print(node.data, end='') 

        node = node.next 

        if node:
            print(sep, end='') 

#Using recursion:
def reversePrint(head):
    if head == None: #empty LList
        return
    reversePrint(head.next) #Recursion will continue until it reaches the end and then starts travelling back
    print(head.data)
    
#Using list slicing:

def reversePrint(head):
    elements = [] #this will be the output
    while(head != None): #if a node exists we append data to elements
        elements.append(head.data) 
        head=head.next
    elements = elements[::-1] #we print elements in reverse order
    
    for element in elements:
        print (element)

