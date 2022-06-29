#creates node class
class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None
#creates empty (head=none) singly linked list class
class SinglyLinkedList:
    def __init__(self):
        self.head = None
#function to print list at the end:
def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)
            
#this is the function they want you to create:
def insertNodeAtTail(head, data):
    current = head #current value is the head
    if head == None: #if the list has no head it is empty
        return SinglyLinkedListNode(data) #return the new node created 
    while current.next != None: #if the current node is not null, we traverse the list to the tail
        current = current.next
    current.next = SinglyLinkedListNode(data)
    return head