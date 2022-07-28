#three possible cases:
#One-> list is empty (head = Null), so we'll need to create new head
#Two-> list has one element, value grater than data we want to add. In this case, we'll need to add a new node and adjust the head accordingly
#Three-> we are inserting in the middle of the list or the end, so we need to traverse list to insertion point. We will also need
#to change pointers to go to the next and previous nodes
#These functions are provided:
import math
import os
import random
import re
import sys

class DoublyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = DoublyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node
            node.prev = self.tail


        self.tail = node

def print_doubly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

#My function:

def sortedInsert(head, data):
    node = DoublyLinkedList(data)
    #case One:
    if head == None:
        head = node
    #case Two:
    elif data < head.data:
        node.next = head
        head.prev = node
        head = node
    #case Three:
    else:
        cur = head  #this is a temporary variable
    #we need to travel to a specific position
        while cur.next != None and cur.data < data:
            cur = cur.next 
        #if we are at the end of the list, we need to insert data at the end:
        if cur.next == None and cur.data < data:
            cur.next = node
            node.prev = cur
        #to insert data at a specific position:
        else:
            previous = cur.prev
        #I need to make changes to previous node (pointing to and from b/c it's coubly linked list):
            previous.next = node
            node.prev = previous
        #I also need to make changes to current node:
            node.next = cur
            cur.prev = node
    
    return head