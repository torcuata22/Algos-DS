def reverse(head):
    prv = None
    cur = head
    next = head.next
    while cur != None:
        next = cur.next
        cur.next = prv
        prv = cur
        cur = next
    head = prv
    return head