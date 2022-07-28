from platform import node


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

def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

class Node(object):
 
    def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

def insertNodeAtPosition(head, data, position):
    if position==0:
        head = Node(data,head)
        return head
    else:
        temp_head = head
        while position>1:
            temp_head = temp_head.next
            position = position -1
        temp_head.next = Node(data,temp_head.next)
        return head
    
#OR:
def insertNodeAtN(head, data, position):
    if head == None:
        head = node
    else:
        temp = head
        count = 1
        while temp != None and count < position:
            temp = temp.next
            count +=1
        node.next = temp.next
        temp.next = node
    return head