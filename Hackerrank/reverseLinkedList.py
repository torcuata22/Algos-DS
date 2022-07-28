def reverse(head):
#start by initializing 3 pointers:
    prv = None
    cur = head
    next = head.next
    while cur != None: #will run as long as the current node is not null
        next = cur.next
        cur.next = prv #changes the direction of the pointer
        prv = cur #these last two shift the nodes
        cur = next
    head = prv
    return head