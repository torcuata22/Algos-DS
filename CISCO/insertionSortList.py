#implement insertion sort algo to a linked list
#we will create dummy node for head so we don't have to deal with null values if creating new head
#we need two pointers: previous and current and to keep track of them, we also need temp variable

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def insertionSortList(self, head:ListNode)->ListNode:
        dummy = ListNode(0,head)
        prev,cur = cur, cur.next 

        while cur:
            if cur.val >=prev.val:
                prev, cur = cur, cur.next 
                continue
            
            temp = head
            while cur.val > temp.next.val:
                temp = temp.next
            prev.next = cur.next 
            cur.next = temp.next 
            cur = prev.next 
        return dummy.next
                
