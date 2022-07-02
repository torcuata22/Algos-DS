#to get the value of a node = position from tail
#will need two pointers. Pointer 1 will traverse to the Position first, then both pointers will traverse together until
#pointer1 reacher the tail. At that point, pointer2 will be at the positionFromTail (see notebook)

def getNode(head, positionFromTail):
    pointer1 = head
    pointer2 = head
    for i in range (positionFromTail):
        pointer1 = pointer1.next
        
    while pointer1.next != None:
        pointer1 = pointer1.next
        pointer2 = pointer2.next
        
    return pointer2.data