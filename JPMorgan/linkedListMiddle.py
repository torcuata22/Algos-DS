#find the middle of a linked list: first, traverse whole list, counting nodes
#n=count/2 and traverse list again until node n

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
 
 
class NodeOperation:
    # Function to add a new node
    def pushNode(self, head_ref, data_val):
 
        # Allocate node and put in the data
        new_node = Node(data_val)
 
        # Link the old list off the new node
        new_node.next = head_ref
 
        # move the head to point to the new node
        head_ref = new_node
        return head_ref
    
    def printNode(self, head):
        while head != None:
            print('%d' % head.data, end="")
            head= head.next
            print("NULL")
            
    def getLen(self, head):
        temp = head
        len = 0
        
        while temp != None:
            len +=1
            temp = temp.next 
        return len
    
    def printMiddle(self,head):
        if head != None:
            len = self.getLen(head)
            temp = head
            middle = len //2
            while middle != 0:
                temp = temp.next
                middle -= 1
            print ("the middle element is [%d]")
            
    

 
 