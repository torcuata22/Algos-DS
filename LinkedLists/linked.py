#create Node, with a value and a reference (initially set to None)
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None #next = None denotes the end of the list
#Traverse linked list
def iter_linked_list(node):
    while node is not None:
        print(node.value)
        node = node.next
        
head = Node("1st Node")
head.next = Node("2nd Node")
head.next.next = Node("3rd Node")
head.next.next.next = Node("4th Node")

#Without loop, I'd do this to print:
#print (head.value)
#print (head.next.value)
#print (head.next.next.value)
        

iter_linked_list(head)
