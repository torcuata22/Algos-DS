#Llist contains cycle if a node is visited more than once. We can detect cycle i two ways:
#Using a dictionary: store node values in dict and if there are any repeated values, then return 1 (cycle) Uses a lot of memory
#Using two pointers: create two pointers, a Fast pointer which will traverse two nodes at a time and a Slow ponter that will traverse
#one node at a time. If the pointers are the same at any point, we have a cycle

def has_cycle(head):
    slow = fast = head #initialize pointers to begin at the same node (the first node)
    while fast!= None and fast.next!= None:
        slow = slow.next
        fast = fast.next.next
        #we check if the POSITION, not the data, are the same:
        if slow == fast: 
            return 1
    return 0
            