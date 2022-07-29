#Given a sorted array (ascending), write a function that turns it into a
#Balanced Binary Search Tree: binary tree in which the depth of tth two
#subtrees of every node never differ by more than 1
#identify middle value, so val <0 to the left and val >0 to the right
#use recursion
#identify left and right pointers (first and last elements of array) and find mid point
#use it as root of tree. elements < mid point go to the left and elements > mid point go to the right
# for each branch, select new mid point and use as root, update pointers until next pointer = null
#time complexity o(n) because it is recursive, space complexity is o(logn)

from logging.config import valid_ident
from turtle import left


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        

def sortedArrayToBST(self, nums:list[int])->TreeNode:
    
        def helper(l,r): #creates tree
            if l > r:
                return None
            m=(l+r)//2 #find mid point
            root = TreeNode(nums[m]) #create the root of the tree at m = midpoint
            root.left = helper(l,m-1) #look only at the elements left of midpoint
            root.right = helper(m+1,r) #looks only at elements right of midpoint
            return root
        
        return helper(0, len(nums)-1)



