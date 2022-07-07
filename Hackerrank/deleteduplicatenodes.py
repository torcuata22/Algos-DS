#to delete repeating values in adyacent nodes: I need to create a temp variable to perform the operations and compare values
#to delete the node, I just skip it
#to compare values store in each node I use head.data

def removeDuplicates(head):
    temp = head
    while temp.next !=None:
        if temp.data == temp.next.data:
            temp.next = temp.next.next
            
        else: 
            temp = temp.next
            
    return head
