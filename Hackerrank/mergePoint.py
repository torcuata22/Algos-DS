def findMergeNode(head1,head2):
    #we need helper function to get the count of the linked list (how many nodes)
    def getcount(head):
        n = 0
        while head.next != None:
            head = head.next 
            n +=1
        return n
    #we need to find the common node, for taht, we use another helper function:
    def getnode(diff,head1, head2):
        #we need to traverse up to diff (difference beteen lengths of both lists)
        for i in range (diff):
            head1 = head1.next 
     #we check the common node:
        while head1 and head2:
            if head1 == head2:
                return head1.data
            else:
                head1 = head1.next 
                head2 = head2.next 
    
    c1 = getcount(head1)
    c2 = getcount(head2)
    #check the difference: 
    if c1 > c2:
        return getnode (c1-c2, head1, head2)
    else:
        return getnode(c2-c1, head2, head1)
            
       
                
    