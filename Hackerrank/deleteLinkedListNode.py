#to delete a node in a linked list you just skip is and Python delestes it automatically
#Two cases: position = head (we skip the head and assign second node as head)
#OR position not head, in whihc case we need to traverse the linked list and find the node we're going to skip
def deleteNode(head, position):
    #case 1: node to delete is the head
    if position == 0:
        head = head.next
    else: 
        #case 2: the node is not the head, so we create temp variable  and counter to traverse
        temp = head
        count = 1
        while temp !=None and count < position: #we travel to the node in the position we want to delete
            temp=temp.next
            count +=1
        temp.next = temp.next.next #once we get there, the loop breaks and we skip the position to delete the node
    return head