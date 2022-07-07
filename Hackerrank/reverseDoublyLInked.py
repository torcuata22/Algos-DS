#To reverse a doubly-linked list we need to reverse the order of the nodes (change next and prev pointers), so the direction of
#the list is reversed. Next becomes prev and viceversa
#To avoid having to use temporary variables, you can do it all in one line

def reverse(head):
    while head.next != None:
        #swap the pointers (all in one line, so no need for temps):
        head.next, head.prev, head = head.prev, head.next, head.next 
        #For the tail node:
    head.next, head.prev = head.prev, None
    return head