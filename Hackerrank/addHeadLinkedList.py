class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None
#creates empty (head=none) singly linked list class
class SinglyLinkedList:
    def __init__(self):
        self.head = None

def insertNodeAtHead(llist, data):
    node = SinglyLinkedListNode(data)
    if llist:
        node.next = llist
    return node