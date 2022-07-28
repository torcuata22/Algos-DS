def compare_lists(head1, head2):
    while head1 != None and head2 != None: 
        #check if both ponters have the same data:
        if head1.data == head2.data:
            head1 = head1.next
            head2 = head2.next
        else:
            return 0
    
    if head1 == None and head2 == None: #check if both lists have the same length
        return 1
    else:
        return 0
    